import importlib.metadata as _metadata

from ._cli import cli
from ._inventory import Group, Host, Inventory, Toml, TomlContainer
from ._service import Service

__all__ = [
    "cli",
    "Service",
    "Toml",
    "TomlContainer",
    "Host",
    "Group",
    "Inventory",
]

__version__ = _metadata.version("masoud")
