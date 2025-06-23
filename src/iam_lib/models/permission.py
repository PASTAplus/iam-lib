"""
:Mod: permission

:Synopsis:
    IAM permission enumeration

:Author:
    Mark Servilla

:Created:
    2025-06-22
"""
from enum import Enum

import daiquiri


logger = daiquiri.getLogger(__name__)


class Permission(Enum):
    READ = "read"
    WRITE = "write"
    CHANGEPERMISSION = "changePermission"
