"""
:Mod: test_rest_wrapper

:Synopsis:
    Pytest for rest_wrapper

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt
import pytest

from iam_lib.rest_api import Client

scheme = "HTTPS"
host = "auth-d.edirepository.org"
public_key_path = "./data/public_key.pem"
private_key_path = "./data/private_key.pem"
algorithm = "ES256"


@pytest.fixture(scope="function")
def client():
    client = Client(
        scheme=scheme,
        host=host,
        public_key_path=public_key_path,
        algorithm=algorithm
    )
    return client


def test_client_init():
    """ Test the initialization of the Client class.
        verb (str): HTTP verb to use
        scheme (str): protocol scheme (http or https)
        host (str): network host domain or address
        token (str): Base64 encoded JWT token of user making request
        accept (str): Accept type either JSON or XML
    """
    token = _make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    client = Client(
        scheme="https",
        host="localhost",
        public_key_path=public_key_path,
        algorithm=algorithm,
    )

    assert client


def test_api_get(client):
    token = _make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    response = client.get(token=token, route="/auth/v1/ping", accept="JSON")
    assert response["status_code"] == 200


def test_api_post(client):
    token = _make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    kwargs = {
        "principal": "EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        "eml": "<eml></eml>"
    }
    response = client.post(token=token, route="/auth/v1/ping", kwargs=kwargs, accept="JSON")
    assert response["status_code"] == 200


def _make_token(exp: datetime) -> str:
    payload = {
        'cn': 'jack',
        'email': None,
        'exp': exp,
        'gn': 'jack',
        'hd': 'edirepository.org',
        'iat': 1746738975,
        'iss': 'https://auth.edirepository.org',
        'nbf': 1746738975,
        'pastaGroups': [],
        'pastaIdentityId': 3,
        'pastaIdpName': 'ldap',
        'pastaIdpUid':'uid=jack,o=EDI,dc=edirepository,dc=org',
        'pastaIsAuthenticated': True,
        'pastaIsEmailEnabled': False,
        'pastaIsEmailVerified': False,
        'pastaIsVetted': True,
        'sn': None,
        'sub': 'EDI-3fa734a7cd6e40998a5c2b5486b6eced'
    }
    token = jwt.encode(payload, Path(private_key_path).read_text().encode("utf-8"), algorithm=algorithm)

    return token

