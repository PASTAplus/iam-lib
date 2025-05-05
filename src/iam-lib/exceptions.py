"""
:Mod: exceptions

:Synopsis:
    IAM-lib level exceptions.

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
import daiquiri

logger = daiquiri.getLogger(__name__)

class IAMLibError(Exception):
    pass


class IAMInvalidUrlError(IAMLibError):
    pass


class IAMParameterError(IAMLibError):
    pass


class IAMTokenError(IAMLibError):
    pass
