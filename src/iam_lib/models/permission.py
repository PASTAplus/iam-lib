"""
:Mod: permission

:Synopsis:
    IAM permission enumeration

:Author:
    Mark Servilla

:Created:
    2025-06-22
"""
from enum import Flag, auto

import daiquiri


logger = daiquiri.getLogger(__name__)


PERMISSION_MAP = ("none", "read", "write", "changePermission")


class Permission(Flag):
    NONE = 0  # "none" - 000 - 0
    READ = auto()  # "read" - 001 - 1
    WRITE = auto()  # "write" - 010 - 2
    CHANGE_PERMISSION = auto()  # "changePermission" - 100 - 4
