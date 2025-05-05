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
import requests

from exceptions import IAMInvalidUrlError, IAMParameterError, IAMTokenError

logger = daiquiri.getLogger(__name__)


class requestsWrapper():
    def __init__(self, url: str, token: dict, **kwargs):

        try:
            urlparse(url)
        except ValueError as e:
            raise IAMInvalidUrlError(e)

        if len(token) == 0:
            msg = f"Invalid token: token cannot be empty"
            raise IAMTokenError(msg)

        # if accept not in ("JSON", "XML"):
        #     msg = f"Invalid accept type {accept}. One of 'JSON' or 'XML' expected."
        #     raise IAMParameterError(msg)
