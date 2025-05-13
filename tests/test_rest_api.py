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
from unittest.mock import MagicMock

import jwt
import pytest
from requests.cookies import RequestsCookieJar  # For mocking
from requests.structures import CaseInsensitiveDict  # For mocking

from iam_lib.client import Client
from iam_lib.response import Response


@pytest.fixture(scope="function")
def client():
    return Client(
        scheme="HTTPS",
        host="localhost",
        public_key_path="./data/public_key.pem",
        algorithm="ES256"
    )


@pytest.fixture(scope="function")
def cookies():
    cookies = RequestsCookieJar()
    cookies.set(
        name="pasta_token",
        value=f"{_make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))}",
        domain="edirepository.org"
    )
    return cookies


@pytest.fixture(scope="function")
def headers():
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    return headers


def test_api_get(client, cookies, headers, mocker):
    token = _make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text='{"GET": "OK"}'
    )
    mock_client_response = Response(mock_requests_response)
    mocker.patch.object(client, "get", return_value=mock_client_response)
    response = client.get(token=token, route="/auth/v1/ping", accept="JSON")
    assert response.status_code == 200
    assert response.body == '{"GET": "OK"}'


def test_api_post(client):
    token = _make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    kwargs = {
        "principal": "EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        "eml": "<eml></eml>"
    }
    response = client.post(token=token, route="/auth/v1/ping", kwargs=kwargs, accept="JSON")
    assert response.status_code == 200


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
    private_key_path = "./data/private_key.pem"
    algorithm = "ES256"
    token = jwt.encode(payload, Path(private_key_path).read_text().encode("utf-8"), algorithm=algorithm)
    return token

