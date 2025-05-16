#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_api

:Synopsis:
    Pytest for API

:Author:
    servilla

:Created:
    5/15/25
"""
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock

import pytest
import requests
from requests.cookies import RequestsCookieJar  # For mocking
from requests.structures import CaseInsensitiveDict  # For mocking

from iam_lib.client import Client
from iam_lib.response import Response
import iam_lib.api.eml as iam_eml
import iam_lib.api.access as iam_access
import iam_lib.api.resource as iam_resource
import iam_lib.api.rule as iam_rule
import iam_lib.api.authorized as iam_authorized
from utilities import make_token


@pytest.fixture(scope="function")
def client():
    return Client(
        scheme="HTTPS",
        host="localhost",
        accept="JSON",
        public_key_path="./data/public_key.pem",
        algorithm="ES256",
        token=make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    )


@pytest.fixture(scope="function")
def cookies():
    cookies = RequestsCookieJar()
    cookies.set(
        name="pasta_token",
        value=f"{make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))}",
        domain="edirepository.org"
    )
    return cookies


@pytest.fixture(scope="function")
def headers():
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    return headers


def test_add_eml(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text='{"ADD_EML": "OK"}'
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    iam_eml.add_eml(
        client=client,
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        eml="<eml></eml>"
    )
    assert client.response.status_code == 200
    assert client.response.body == '{"ADD_EML": "OK"}'


def test_add_access(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text='{"ADD_ACCESS": "OK"}'
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    iam_access.add_access(
        client=client,
        access="<access></access>",
        resource_key="api_service_xyz",
        resource_label="api_service_xyz",
        resource_type="service"
    )
    assert client.response.status_code == 200
    assert client.response.body == '{"ADD_ACCESS": "OK"}'