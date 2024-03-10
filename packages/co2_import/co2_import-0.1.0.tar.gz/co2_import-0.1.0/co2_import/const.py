from enum import Enum
from pathlib import Path
from typing import List, Tuple

from co2.const import Settings as SettingsInherit

_path = Path(__file__).absolute().parent


class Settings(SettingsInherit):
    REQUIRED_ODOO_MODULE: List[str] = [
        "onsp_co2_account_asset_management",
        "account_asset_management",
        "onsp_co2",
    ]

    # module_name, git link (with .git at the end), branch
    GIT_REPOS: Tuple[Tuple[str, str, str], ...] = [
        (
            "onsp_co2_bundle",
            "git@github.com:MyCityCO2/mycityco2-engine.git",
            "16.0",
        ),
        (
            "account-financial-tools",
            "git@github.com:OCA/account-financial-tools.git",
            "16.0",
        ),
        ("reporting-engine", "git@github.com:OCA/reporting-engine.git", "16.0"),
    ]
    GIT_PATH: Path = _path / "data" / "modules"

    DOCKER_CONTAINER_PREFIX: str = "co2_import_container_"
    DOCKER_ODOO_CONTAINER_NAME: str = DOCKER_CONTAINER_PREFIX + "odoo"
    DOCKER_POSTGRES_CONTAINER_NAME: str = DOCKER_CONTAINER_PREFIX + "db"

    DOCKER_NETWORK_NAME: str = "co2_import_network"

    DOCKER_ODOO_IMAGE: str = "odoo:16.0"
    DOCKER_POSTGRES_IMAGE: str = "postgres:13"

    ODOO_CONF_PATH: Path = _path / "data" / "odoo.conf"


settings: Settings = Settings()


class RemoteType(str, Enum):
    remote = "remote"
    local = "local"
