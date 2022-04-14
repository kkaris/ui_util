import configparser
from os import environ
from pathlib import Path
from typing import Optional

__all__ = [
    "get_indra_conf",
]


def get_indra_conf(key: str, missing_ok: bool = True) -> Optional[str]:
    """Get a value from the indra.conf file.

    Parameters
    ----------
    key :
        The key to look for in the config file.
    missing_ok :
        If True, return None if the key is not found.
        If False, raise a KeyError if the key is not found.

    Returns
    -------
    :
        The value corresponding to the key if found.
    """
    try:
        if key in environ:
            return environ[key]
        path = Path.home().joinpath(".config", "indra", "config.ini")
        if not path.is_file():
            return None
        cfp = configparser.ConfigParser()
        cfp.read(path)
        return cfp.get("indra", key)
    except Exception:
        if missing_ok:
            return None
        raise KeyError(f"'{key}' not found in config")
