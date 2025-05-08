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

class IAMLibException(Exception):
    pass


class IAMInvalidAccept(IAMLibException):
    pass


class IAMInvalidHost(IAMLibException):
    pass


class IAMInvalidScheme(IAMLibException):
    pass


class IAMInvalidUrl(IAMLibException):
    pass


class IAMInvalidVerb(IAMLibException):
    pass


class IAMInvalidParameter(IAMLibException):
        pass


class IAMInvalidToken(IAMLibException):
    pass
