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

import iam_lib.exceptions
from iam_lib.config import Config

logger = daiquiri.getLogger(__name__)


class RequestsWrapper:
    """Wrapper for IAM-specific use of the requests package.

    Wraps the requests package to provide IAM-specific functionality.

    """
    def __init__(self, verb: str, url: str, token: str, accept: str, kwargs: dict):
        """__init__
        Args:
            verb (str): HTTP verb to use
            url (str): Auth target URL
            token (str): Base64 encoded JWT token of requesting user profile
            accept (str): Accept type either JSON or XML
            kwargs (dict): Additional POST or PUT arguments as key/value pairs
        """

        self.verb = _validate_verb(verb)
        self.url = _validate_url(url)
        self.token = _validate_token(token)
        self.accept = _validate_accept(accept)
        self.kwargs = _validate_kwargs(kwargs)


def _validate_verb(verb: str) -> str:
    if verb.lower() not in ("get", "post", "put", "delete"):
        raise iam_lib.exceptions.IAMInvalidUrl(f"Invalid HTTP verb '{verb}'")
    return verb.lower()


def _validate_url(url: str) -> str:
    try:
        result = urlparse(url)
        if result.scheme not in ("http", "https"):
            msg = f"Invalid URL: scheme '{url}' should be 'http' or 'https'"
            raise iam_lib.exceptions.IAMInvalidUrl(msg)
        if result.netloc not in Config.ALLOWED_HOSTS:
            msg = f"Invalid URL: hostname '{url}' should be one of '{",".join([_ for _ in Config.ALLOWED_HOSTS])}'"
            raise iam_lib.exceptions.IAMInvalidUrl(msg)
    except ValueError as e:
        raise iam_lib.exceptions.IAMInvalidUrl(e)
    return url

def _validate_token(token: str) -> str:
    return token

def _validate_accept(accept: str) -> str:
    if accept.lower() not in ("json", "xml"):
        raise iam_lib.exceptions.IAMInvalidAccept(f"Invalid accept type '{accept}': must be 'json' or 'xml'")
    return "application/" + accept.lower()

def _validate_kwargs(kwargs: dict) -> dict:
    for key,value in kwargs.items():
        if key not in Config.VALID_KWARGS:
            raise iam_lib.exceptions.IAMParameterError(f"Invalid keyword argument '{key}'")
        if key == "descendants":
            if value not in ("True", "False"):
                raise iam_lib.exceptions.IAMParameterError(f"Invalid keyword argument for 'descendants': value '{value}' must be True or False")
        if key == "permission":
            if value not in ("read", "write", "changePermission"):
                raise iam_lib.exceptions.IAMParameterError(f"Invalid keyword argument for 'permission': value '{value}' must be 'read', 'write', or 'changePermission'")
    return kwargs
