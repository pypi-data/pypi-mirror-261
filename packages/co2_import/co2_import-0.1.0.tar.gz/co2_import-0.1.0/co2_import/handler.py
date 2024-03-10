import time
from enum import Enum

import docker
import docker.errors as docker_errors
import psycopg2
import typer
from docker.types import Mount
from loguru import logger
from otools_rpc.external_api import Environment

from co2_import.const import RemoteType, settings
from co2_import.utils import repos


class Handler:
    def __init__(
        self,
        type: Enum,
        user: str = False,
        password: str = False,
        db: str = False,
        url: str = False,
        sql_port: str = False,
        sql_user: str = False,
        sql_host: str = False,
        sql_password: str = False,
        *args,
        **kwargs,
    ):
        self._type = type
        self._user = user
        self._password = password
        self._db = db
        self._url = url

        self._sql_port = sql_port
        self._sql_user = sql_user
        self._sql_host = sql_host
        self._sql_password = sql_password

        # Docker env variables
        self.client = (
            self._containers_name_mapping
        ) = self._CONTAINERS = self._network_name_mapping = self._network_name = False

    def setup(self):
        match self._type:
            case RemoteType.local:
                self._setup_local_remote()
            case RemoteType.remote:
                self._setup_remote_remote()
            case _:
                raise NotImplementedError("This features is not implemented yet")

    def clean_local(self):
        self._docker_get_client()
        self._docker_get_mapping()

        for container_name in self._CONTAINERS:
            if self._containers_name_mapping.get(container_name):
                logger.debug(
                    f"[DOCKER] Stopping and deleting container {container_name}"
                )
                self.client.containers.get(container_name).remove(force=True)

        if self._network_name_mapping.get(self._network_name):
            logger.debug(f"[DOCKER] Stopping and deleting network {self._network_name}")
            self.client.networks.get(settings.DOCKER_NETWORK_NAME).remove()

    def _docker_get_mapping(self):
        if not self._containers_name_mapping:
            self._containers_name_mapping = {
                container.name: container
                for container in self.client.containers.list(all=True)
            }
        if not self._CONTAINERS:
            self._CONTAINERS = [
                settings.DOCKER_ODOO_CONTAINER_NAME,
                settings.DOCKER_POSTGRES_CONTAINER_NAME,
            ]

        if not self._network_name_mapping:
            self._network_name_mapping = {
                network.name: network for network in self.client.networks.list()
            }
        if not self._network_name:
            self._network_name = settings.DOCKER_NETWORK_NAME

    def _docker_get_client(self):
        if not self.client:
            self.client = docker.from_env()
        return self.client

    def env(self, dbname: str = False):
        return Environment(
            url=self._url,
            username=self._user,
            password=self._password,
            db=dbname,
            auto_auth=False,
            logger=logger,
            cache_no_expiration=True,
        )

    def _docker_setup_var(self):
        self._user = "admin"
        self._password = "adminadminadmin"
        self._url = "http://localhost:8069"

        self._sql_port = 5432
        self._sql_user = "odoo"
        self._sql_host = "localhost"
        self._sql_password = "odoo"

    def _setup_local_remote(self):
        if self._type is not RemoteType.local:
            raise RuntimeError(
                "This shouldn't be possible. Calling the remote local with remote remote ?"
            )

        # Docker Setup
        self._docker_setup_var()

        self._docker_get_client()
        self._docker_get_mapping()

        repos.clone_repos(settings.GIT_REPOS)

        if not self._network_name_mapping.get(self._network_name):
            logger.debug(f"[DOCKER] Creating {self._network_name} network")
            self._network_name_mapping[
                self._network_name
            ] = self.client.networks.create(
                name=self._network_name,
                driver="bridge",
                check_duplicate=True,
                attachable=True,
                scope="global",
            )

        network = self._network_name_mapping[self._network_name]

        def _create_docker_container(
            image, container, port, env=False, mounts=False, command=False
        ):
            container_name = container.split(settings.DOCKER_CONTAINER_PREFIX)[-1]
            try:
                self.client.images.get(image)
            except docker_errors.ImageNotFound:
                self.client.images.pull(image)
            except Exception as e:
                raise e
            con = self.client.containers.create(
                image,
                name=container,
                network=network.name,
                hostname=container_name,
                ports=port,
                tty=True,
                environment=env if env else None,
                mounts=mounts if mounts else None,
                command=command if command else None,
            )
            self._containers_name_mapping[container] = con
            return con

        for container in self._CONTAINERS:
            container_name = container.rsplit(
                settings.DOCKER_CONTAINER_PREFIX, maxsplit=1
            )[-1]
            if not self._containers_name_mapping.get(container):
                logger.debug(f"[DOCKER] Creating {container_name} docker")

                match container:
                    case settings.DOCKER_POSTGRES_CONTAINER_NAME:
                        _create_docker_container(
                            container=container,
                            image=settings.DOCKER_POSTGRES_IMAGE,
                            port={
                                "5432/tcp": [{"HostIp": "0.0.0.0", "HostPort": "5432"}]
                            },
                            env={
                                "POSTGRES_DB": "postgres",
                                "POSTGRES_PASSWORD": "odoo",
                                "POSTGRES_USER": "odoo",
                            },
                        )

                    case settings.DOCKER_ODOO_CONTAINER_NAME:
                        _mount_path_docker = "/mnt/extra-addons/"
                        addons = [
                            _mount_path_docker + addon
                            for addon, _, _ in settings.GIT_REPOS
                        ]
                        _create_docker_container(
                            container=container,
                            command=f"-c /var/lib/odoo/odoo.conf --addons-path {','.join(addons)}",
                            image=settings.DOCKER_ODOO_IMAGE,
                            port={
                                "8069/tcp": [{"HostIp": "0.0.0.0", "HostPort": "8069"}]
                            },
                            mounts=[
                                Mount(
                                    source=settings.ODOO_CONF_PATH.as_posix(),
                                    target="/var/lib/odoo/odoo.conf",
                                    type="bind",
                                ),
                                Mount(
                                    source=settings.GIT_PATH.as_posix(),
                                    target=_mount_path_docker,
                                    type="bind",
                                ),
                            ],
                        )

            if self._containers_name_mapping.get(container):
                container_docker = self._containers_name_mapping.get(container)

                if container_docker.status != "running":
                    logger.debug(f"[DOCKER] Starting {container_name} docker")
                    try:
                        container_docker.start()
                    except docker_errors.APIError:
                        logger.error(
                            f"[DOCKER] The container '{container}' could not start, please check if port is already used."
                        )
                        raise typer.Abort()
                container_docker.reload()

    def change_superuser_state(self, dbname: str, state: bool = False) -> int:
        with psycopg2.connect(
            database=dbname,
            port=self._sql_port,
            host=self._sql_host,
            user=self._sql_user,
            password=self._sql_password,
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(f"update res_users set active = {state} where id = 1;")
            connection.commit()

            logger.debug(
                f"The database {dbname} have now the superuser '{'Enabled' if state else 'Disabled'}'"
            )
            return cursor.rowcount

    def is_odoo_ready(self, dbname: str = False) -> bool:
        while True:
            try:
                self.env(dbname).env.common.version()
                return True
            except (ConnectionRefusedError, ConnectionResetError):
                time.sleep(1)
                continue
            except Exception as err:
                logger.error(f"Odoo server not running {err}")
                return False

    def _setup_remote_remote(self):
        raise NotImplementedError("This features is not implemented yet")
