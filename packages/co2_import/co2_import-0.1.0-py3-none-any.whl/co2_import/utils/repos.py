import os
from typing import Tuple

from loguru import logger

from co2_import.const import settings
from co2_import.utils.git import Git


def clone_repos(git_repos: Tuple[Tuple[str, str], ...]) -> bool:
    logger.info(f"Ensuring all {len(git_repos)} git repos")
    for module_name, origin_url, branch in git_repos:
        path = settings.GIT_PATH / module_name
        if path.exists():
            Git.pull(path=path, branch=branch, depth=1)
        if not os.path.isdir(path):
            Git.clone(path=path, url=origin_url, branch=branch, depth=1)
