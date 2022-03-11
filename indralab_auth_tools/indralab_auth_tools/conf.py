import configparser
from os import environ
from pathlib import Path
from typing import Optional

__all__ = [
    "get_indra_conf",
]


def get_indra_conf(key: str) -> Optional[str]:
    if key in environ:
        return environ[key]
    path = Path.home().joinpath(".config", "indra", "config.ini")
    if not path.is_file():
        return None
    cfp = configparser.ConfigParser()
    cfp.read(path)
    return cfp.get("indra", key)
