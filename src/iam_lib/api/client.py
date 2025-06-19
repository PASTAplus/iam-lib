"""
:Mod: client

:Synopsis:
    IAM REST API HTTP request client

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
from pathlib import Path

import daiquiri
import requests
import jwt

import iam_lib.exceptions
import iam_lib.token


logger = daiquiri.getLogger(__name__)


class Client:
    """IAM REST API client"""

    def __init__(
            self,
            scheme: str,
            host: str,
            accept: str,
            public_key_path: str,
            algorithm: str,
            token: str,
            truststore: str = None,
    ):
        """Initialize client instance

        Args:
            scheme (str): protocol scheme (http or https)
            host (str):  authentication host domain or address
            accept (str): accept type (JSON or XML)
            public_key_path (str): path to token signing public key
            algorithm (str): token signing algorithm
            token (str): IAM JWT authentication token
            truststore (str): path to truststore (defaults to None)

        Raises:
            iam_lib.exceptions.IAMInvalidScheme
            iam_lib.exceptions.IAMInvalidHost
            iam_lib.exceptions.IAMInvalidAccept
            iam_lib.exceptions.IAMInvalidPublicKey
            iam_lib.exceptions.IAMInvalidToken
        """

        self._scheme = _validate_scheme(scheme)
        self._host = _validate_host(host)
        self._accept = _validate_accept(accept)
        self._public_key_path = _validate_public_key_path(public_key_path)
        self._algorithm = algorithm
        self._token = _validate_token(token, public_key_path, algorithm)
        self._truststore = _validate_truststore(truststore)
        self._cookies = {"pasta_token": token}
        self._response = None

    @property
    def scheme(self) -> str:
        return self._scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self._scheme = _validate_scheme(scheme)

    @property
    def host(self) -> str:
        return self._host

    @host.setter
    def host(self, host: str):
        self._host = _validate_host(host)

    @property
    def accept(self) -> str:
        return self._accept

    @accept.setter
    def accept(self, accept: str):
        self._accept = _validate_accept(accept)

    @property
    def public_key_path(self) -> str:
        return self._public_key_path

    @public_key_path.setter
    def public_key_path(self, public_key_path: str):
        self._public_key_path = _validate_public_key_path(public_key_path)

    @property
    def algorithm(self) -> str:
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm: str):
        self._algorithm = algorithm

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, token: str):
        self._token = _validate_token(token, self._public_key_path, self._algorithm)

    @property
    def truststore(self) -> str:
        return self._truststore

    @truststore.setter
    def truststore(self, truststore: str):
        self._truststore = _validate_truststore(truststore)

    @property
    def response(self) -> None | requests.Response:
        return self._response

    def post(self, route: str, form_params: dict = None) -> requests.Response:
        """Send a POST request to the IAM REST API

        Args:
            route (str): IAM route
            form_params (dict): IAM POST form parameters

        Returns:
            response (requests.Response): requests response object
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
         """
        if form_params is None: form_params = {}
        _validate_parameters(form_params, self._public_key_path, self._algorithm)
        url = self.scheme + "://" + self.host + "/" + route
        try:
            self._response = requests.post(
                url,
                json=form_params,
                cookies=self._cookies,
                headers={"Accept-Type": f"{self._accept}"},
                verify=self._truststore,
            )
        except requests.exceptions.RequestException as e:
            raise iam_lib.exceptions.IAMRequestError(e)
        if self._response.status_code != 200:
            raise iam_lib.exceptions.IAMResponseError(self._response)
        return self._response

    def put(self, route: str, form_params: dict = None) -> requests.Response:
        """Send a PUT request to the IAM REST API

        Args:
            route (str): IAM route
            form_params (dict): IAM POST form parameters

        Returns:
            response (requests.Response): requests response object
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
         """
        if form_params is None: form_params = {}
        _validate_parameters(form_params, self._public_key_path, self._algorithm)
        url = self.scheme + "://" + self.host + "/" + route
        try:
            self._response = requests.put(
                url,
                json=form_params,
                cookies=self._cookies,
                headers={"Accept-Type": f"{self._accept}"},
                verify=self._truststore,
            )
        except requests.exceptions.RequestException as e:
            raise iam_lib.exceptions.IAMRequestError(e)
        if self._response.status_code != 200:
            raise iam_lib.exceptions.IAMResponseError(self._response)
        return self._response

    def get(self, route: str, query_params: dict = None) -> requests.Response:
        """Send a GET request to the IAM REST API

        Args:
            query_params (dict): IAM GET query parameters (optional)
            route (str): IAM route

        Returns:
            response (requests.Response): requests response object
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
         """
        if query_params is None: query_params = {}
        url = self.scheme + "://" + self.host + "/" + route
        try:
            self._response = requests.get(
                url,
                params=query_params,
                cookies=self._cookies,
                headers={"Accept-Type": f"{self._accept}"},
                verify=self._truststore,
            )
        except requests.exceptions.RequestException as e:
            raise iam_lib.exceptions.IAMRequestError(e)
        if self._response.status_code != 200:
            raise iam_lib.exceptions.IAMResponseError(self._response)
        return self._response

    def delete(self, route: str) -> requests.Response:
        """Send a DELETE request to the IAM REST API

        Args:
            route (str): IAM route

        Returns:
            response (Response): Generic response object
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
         """
        url = self.scheme + "://" + self.host + "/" + route
        try:
            self._response = requests.delete(
                url,
                cookies=self._cookies,
                headers={"Accept-Type": f"{self._accept}"},
                verify=self._truststore,
            )
        except requests.exceptions.RequestException as e:
            raise iam_lib.exceptions.IAMRequestError(e)
        if self._response.status_code != 200:
            raise iam_lib.exceptions.IAMResponseError(self._response)
        return self._response


def _validate_token(token: str, public_key_path: str, algorithm: str) -> str:
    public_key = Path(public_key_path).read_text().encode("utf-8")
    try:
        jwt.decode(token, public_key, algorithms=algorithm)
    except jwt.InvalidTokenError as e:
        raise iam_lib.exceptions.IAMInvalidToken(f"Invalid token: {e}")
    return token


def _validate_public_key_path(public_key_path: str) -> str:

    if Path(public_key_path).exists() and Path(public_key_path).is_file():
        return public_key_path
    else:
        msg = f"Public key file '{public_key_path}' does not exist"
        raise iam_lib.exceptions.IAMInvalidPublicKey(msg)


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
    hostname = host.split(":")[0]  # Disregard port if specified
    if hostname not in valid_hosts:
        msg = f"Invalid host '{host}': must be one of '{", ".join(valid_hosts)}'"
        raise iam_lib.exceptions.IAMInvalidHost(msg)
    return host


def _validate_accept(accept: str) -> str:
    if accept.lower() not in ("json", "xml"):
        raise iam_lib.exceptions.IAMInvalidAccept(f"Invalid accept type '{accept}': must be 'json' or 'xml'")
    return "application/" + accept.lower()


def _validate_parameters(parameters: dict, public_key_path: str, algorithm: str) -> dict:
    valid_parameters = (
        "principal",  # EDI-ID (must begin with "edi-")
        "sub",  # EDI-ID (must begin with "edi-")
        "eml",  # EML document (XML)
        "access",  # EML access element (XML)
        "resource_key",  # Resource key (unique identifier)
        "resource_label",  # Resource label (non-unique)
        "resource_type",  # Resource type (enumerated set: collection, package, eml, report, data, ezeml, ...)
        "parent_resource_key",  # Resource key of parent
        "descendants",  # Boolean (True or False)
        "permission",  # Resource permission (enumerated set: read, write, or changePermission)
        "token",  # Base64 encoded JWT token of the client
        "given_name",  # Given name
        "family_name",  # Family name
        "email",  # Email address
    )
    for key,value in parameters.items():
        if key not in valid_parameters:
            raise iam_lib.exceptions.IAMInvalidParameter(f"Invalid keyword argument '{key}'")
        if key in ("ancestors", "descendants", "all"):
            if value not in ("True", "False"):
                msg = f"Invalid keyword argument for '{key}': value '{value}' must be True or False"
                raise iam_lib.exceptions.IAMInvalidParameter(msg)
        if key == "permission":
            if value not in ("read", "write", "changePermission"):
                msg = f"Invalid keyword argument for 'permission': value '{value}' must be 'read', 'write', or 'changePermission'"
                raise iam_lib.exceptions.IAMInvalidParameter(msg)
        if key == "token":
            _validate_token(value, public_key_path, algorithm)
    return parameters


def _validate_truststore(truststore: str | None) -> str | bool:
    if truststore is None:
        return True  # Verify certificates using Python CA bundle
    else:
        if Path(truststore).exists() and Path(truststore).is_file():
            return truststore
        else:
            msg = f"Truststore file '{truststore}' does not exist"
            raise iam_lib.exceptions.IAMInvalidParameter(msg)
