"""
:Mod: test_client

:Synopsis:
    Pytest for the client API

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
from pathlib import Path
from unittest.mock import MagicMock

import daiquiri
import jwt
import requests

from tests.config import Config


logger = daiquiri.getLogger(__name__)


def test_client(client):
    assert Config.SCHEME.lower() == client.scheme.lower()
    assert Config.AUTH_HOST == client.host
    assert Config.ACCEPT.lower() in client.accept.lower()
    assert Config.PUBLIC_KEY_PATH == client.public_key_path
    assert Config.JWT_ALGORITHM == client.algorithm
    jwt.decode(
        client.token,
        Path(client.public_key_path).read_text().encode("utf-8"),
        algorithms=client.algorithm
    )

def test_get(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"GET\": \"OK\"}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    response = client.get(route="auth/v1/ping")
    assert response.status_code == 200
    assert response.text == "{\"GET\": \"OK\"}"


def test_post(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"POST\": \"OK\"}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    parameters = {
        "principal": "EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        "eml": "<eml></eml>"
    }
    response = client.post(route="auth/v1/ping", form_params=parameters)
    assert response.status_code == 200
    assert response.text == "{\"POST\": \"OK\"}"


def test_put(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"PUT\": \"OK\"}"
    )
    mocker.patch.object(requests, "put", return_value=mock_requests_response)
    parameters = {
        "principal": "EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        "eml": "<eml></eml>"
    }
    response = client.put(route="auth/v1/ping", form_params=parameters)
    assert response.status_code == 200
    assert response.text == "{\"PUT\": \"OK\"}"


def test_delete(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"DELETE\": \"OK\"}"
    )
    mocker.patch.object(requests, "delete", return_value=mock_requests_response)
    response = client.delete(route="auth/v1/ping")
    assert response.status_code == 200
    assert response.text == "{\"DELETE\": \"OK\"}"
