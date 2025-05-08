"""
:Mod: requests_wrapper

:Synopsis:
    IAM wrapper around the requests package

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
from pathlib import Path
from urllib.parse import urlparse

import daiquiri
import jwt
import requests

import iam_lib.exceptions


logger = daiquiri.getLogger(__name__)


class RequestsWrapper:
    """Wrapper for IAM-specific use of the requests package.

    Wraps the requests package to provide IAM-specific functionality.

    """
    def __init__(
            self,
            verb: str, # HTTP verb to use
            scheme: str, # protocol scheme (http or https)
            host: str, # network host domain or address
            token: str, # Base64 encoded JWT token of user making request
            public_key: bytes, # Token signing public key
            algorithm: str, # Token signing algorithm
            accept: str # Accept type either JSON or XML
    ):

        self.verb = _validate_verb(verb)
        self.scheme = _validate_scheme(scheme)
        self.host = _validate_host(host)
        self.token = _validate_token(token, public_key, algorithm)
        self.accept = _validate_accept(accept)


def _validate_verb(verb: str) -> str:
    if verb.lower() not in ("get", "post", "put", "delete"):
        raise iam_lib.exceptions.IAMInvalidUrl(f"Invalid HTTP verb '{verb}'")
    return verb.lower()


def _validate_scheme(scheme: str) -> str:
    if scheme.lower() not in ("http", "https"):
        raise iam_lib.exceptions.IAMInvalidScheme(f"Invalid URL: scheme '{scheme}' should be 'http' or 'https'")
    return scheme.lower()


def _validate_host(host: str) -> str:
    allowed_hosts = (
        "localhost",
        "127.0.0.1",
        "auth.edirepository.org",
        "auth-s.edirepository.org",
        "auth-d.edirepository.org"
    )
    if host not in allowed_hosts:
        msg = f"Invalid host '{host}': must be one of '{", ".join(allowed_hosts)}'"
        raise iam_lib.exceptions.IAMInvalidHost(msg)
    return host


def _validate_token(token: str, public_key: bytes, algorithm: str) -> str:
    try:
        jwt_token = jwt.decode(token, public_key, algorithms=algorithm)
    except jwt.InvalidTokenError as e:
        raise iam_lib.exceptions.IAMInvalidToken(f"Invalid token: {e}")
    return token


def _validate_accept(accept: str) -> str:
    if accept.lower() not in ("json", "xml"):
        raise iam_lib.exceptions.IAMInvalidAccept(f"Invalid accept type '{accept}': must be 'json' or 'xml'")
    return "application/" + accept.lower()


def _validate_kwargs(kwargs: dict) -> dict:
    valid_kwargs = (
        "principal",            # EDI-ID (must begin with "edi-")
        "eml",                  # EML document (XML)
        "access",               # EML access element (XML)
        "resource_key",         # Resource key (unique identifier)
        "resource_label",       # Resource label (non-unique)
        "resource_type",        # Resource type (enumerated set: collection, package, eml, report, data, ezeml, ...)
        "parent_resource_key",  # Resource key of parent
        "descendants",          # Boolean (True or False)
        "permission",           # Resource permission (enumerated set: read, write, or changePermission)
        "token"                 # Base64 encoded JWT token of the client
    )
    for key,value in kwargs.items():
        if key not in valid_kwargs:
            raise iam_lib.exceptions.IAMInvalidParameter(f"Invalid keyword argument '{key}'")
        if key == "descendants":
            if value not in ("True", "False"):
                raise iam_lib.exceptions.IAMInvalidParameter(f"Invalid keyword argument for 'descendants': value '{value}' must be True or False")
        if key == "permission":
            if value not in ("read", "write", "changePermission"):
                raise iam_lib.exceptions.IAMInvalidParameter(f"Invalid keyword argument for 'permission': value '{value}' must be 'read', 'write', or 'changePermission'")
    return kwargs
