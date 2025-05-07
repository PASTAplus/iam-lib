"""
:Mod: requests_wrapper

:Synopsis:
    IAM wrapper around the requests package

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
from urllib.parse import urlparse

import daiquiri
import jwt
import requests

from iam_lib.exceptions import IAMInvalidUrlError, IAMParameterError, IAMTokenError

logger = daiquiri.getLogger(__name__)


class RequestsWrapper():
    """Wrapper for IAM-specific use of the requests package.

    Wraps the requests package to provide IAM-specific functionality.

    """
    def __init__(self, url: str, token: str, kwargs: dict):

        print("\n")

        print(url)

        breakpoint()
        
        try:
            urlparse(url)
        except ValueError as e:
            raise IAMInvalidUrlError(e)

        print(token)
        
        if len(token) == 0:
            msg = "Invalid token: token cannot be empty"
            raise IAMTokenError(msg)

        for key, value in kwargs.items():
            print(f"{key}: {value}")

