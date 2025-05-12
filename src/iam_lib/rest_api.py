"""
:Mod: rest_api

:Synopsis:
    IAM REST API HTTP request client

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
from pathlib import Path
from urllib.parse import urlparse

import daiquiri
import requests

from iam_lib.response import Response
import iam_lib.exceptions
import iam_lib.token

logger = daiquiri.getLogger(__name__)


class Client:
    """IAM REST API client"""

    def __init__(
            self,
            scheme: str, # protocol scheme (http or https)
            host: str, # network host domain or address
            public_key_path: str, # Path to public key
            algorithm: str, # Token signing algorithm
    ):

        self.scheme = _validate_scheme(scheme)
        self.host = _validate_host(host)
        self.public_key = _validate_public_key(Path(public_key_path))
        self.algorithm = algorithm

    def post(self, token: str, route: str, kwargs: dict, accept: str) -> Response:
        """Send a POST request to the IAM REST API

        Args:
            token (str): IAM JWT token
            route (str): IAM route
            kwargs (dict): IAM POST request key/value pairs
            accept (str): IAM POST accept type (either JSON or XML)
         """
        iam_lib.token.validate(token, self.public_key, self.algorithm)
        _validate_route(route)
        _validate_accept(accept)
        cookies = {"pasta_token": token}
        url = self.scheme + "://" + self.host + "/" + route
        try:
            request = requests.post(url, data=kwargs, cookies=cookies, headers={"Accept-Type": f"{accept}"})
        except requests.exceptions.RequestException as e:
            raise iam_lib.exceptions.IAMRequestError(e)
        response = Response(request)
        if response.status_code != 200:
            raise iam_lib.exceptions.IAMResponseError(response)
        return response

    def put(self, token: str, route: str, kwargs: dict, accept: str) -> Response:
        """Send a PUT request to the IAM REST API

        Args:
            token (str): IAM JWT token
            route (str): IAM route
            kwargs (dict): IAM POST request key/value pairs
            accept (str): IAM POST accept type (either JSON or XML)
         """
        iam_lib.token.validate(token, self.public_key, self.algorithm)
        _validate_route(route)
        _validate_accept(accept)
        cookies = {"pasta_token": token}
        url = self.scheme + "://" + self.host + "/" + route
        try:
            request = requests.put(url, data=kwargs, cookies=cookies, headers={"Accept-Type": f"{accept}"})
        except requests.exceptions.RequestException as e:
            raise iam_lib.exceptions.IAMRequestError(e)
        response = Response(request)
        if response.status_code != 200:
            raise iam_lib.exceptions.IAMResponseError(response)
        return response

    def get(self, token: str, route: str, accept: str) -> Response:
        """Send a GET request to the IAM REST API

        Args:
            token (str): IAM JWT token
            route (str): IAM route
            accept (str): IAM POST accept type (either JSON or XML)
         """
        iam_lib.token.validate(token, self.public_key, self.algorithm)
        _validate_route(route)
        _validate_accept(accept)
        cookies = {"pasta_token": token}
        url = self.scheme + "://" + self.host + "/" + route
        try:
            request = requests.get(url, cookies=cookies, headers={"Accept-Type": f"{accept}"})
        except requests.exceptions.RequestException as e:
            raise iam_lib.exceptions.IAMRequestError(e)
        response = Response(request)
        if response.status_code != 200:
            raise iam_lib.exceptions.IAMResponseError(response)
        return response

    def delete(self, token: str, route: str, accept: str) -> Response:
        """Send a DELETE request to the IAM REST API

        Args:
            token (str): IAM JWT token
            route (str): IAM route
            accept (str): IAM POST accept type (either JSON or XML)
         """
        iam_lib.token.validate(token, self.public_key, self.algorithm)
        _validate_route(route)
        _validate_accept(accept)
        cookies = {"pasta_token": token}
        url = self.scheme + "://" + self.host + "/" + route
        try:
            request = requests.delete(url, cookies=cookies, headers={"Accept-Type": f"{accept}"})
        except requests.exceptions.RequestException as e:
            raise iam_lib.exceptions.IAMRequestError(e)
        response = Response(request)
        if response.status_code != 200:
            raise iam_lib.exceptions.IAMResponseError(response)
        return response


def _validate_public_key(public_key_path: Path) -> bytes:
    if public_key_path.exists() and public_key_path.is_file():
        return public_key_path.read_text().encode("utf-8")
    else:
        msg = f"Public key file '{public_key_path}' does not exist"
        raise iam_lib.exceptions.IAMInvalidPublicKey(msg)


def _validate_route(route: str) -> str:
    valid_routes = (
        "/auth/v1/ping",
        "/auth/v1/eml",
        "/auth/v1/access"
    )
    if route not in valid_routes:
        msg = f"Invalid route: '{route}'"
        raise iam_lib.exceptions.IAMInvalidRoute(msg)
    return route

def _validate_scheme(scheme: str) -> str:
    if scheme.lower() not in ("http", "https"):
        raise iam_lib.exceptions.IAMInvalidScheme(f"Invalid URL: scheme '{scheme}' should be 'http' or 'https'")
    return scheme.lower()


def _validate_host(host: str) -> str:
    valid_hosts = (
        "localhost",
        "127.0.0.1",
        "auth.edirepository.org",
        "auth-s.edirepository.org",
        "auth-d.edirepository.org"
    )
    if host not in valid_hosts:
        msg = f"Invalid host '{host}': must be one of '{", ".join(valid_hosts)}'"
        raise iam_lib.exceptions.IAMInvalidHost(msg)
    return host


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
