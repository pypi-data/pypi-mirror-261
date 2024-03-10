from pathlib import Path
from typing import Optional

import typer
from loguru import logger

from co2_import.const import RemoteType
from co2_import.handler import Handler

cli = typer.Typer(no_args_is_help=True)


@cli.command(
    help="This command is used to create all docker if type is local and also to run the import script"
)
def run(
    path: Optional[Path] = typer.Option(
        Path("co2-output"),
        "-p",
        "--path",
        exists=False,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=False,
        resolve_path=True,
        help="Where do you want to save the output file ?",
    ),
    type: RemoteType = typer.Option(RemoteType.local, case_sensitive=False),
):
    if not path.exists():
        logger.error(f"The path you provided doesn't exist. {path}")
        raise typer.Abort()

    handler = Handler(type=type)
    handler.setup()


@cli.command(help="Delete all container related to co2_import")
def clean(
    force: bool = typer.Option(
        False, "-f", "--force", help="This option is there to remove confirmation"
    )
):
    do_delete = force
    if not do_delete:
        do_delete = typer.confirm(
            "Do you really want to delete all container and network created by us ?"
        )

    if not do_delete:
        raise typer.Abort()

    logger.info("Cleaning all container and network created by co2_import...")
    Handler(type=RemoteType.local).clean_local()
