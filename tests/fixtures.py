#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    fixtures

:Synopsis:
    Pytest fixtures

:Author:
    servilla

:Created:
    5/16/25
"""
from datetime import datetime, timedelta, timezone

import pytest
from requests.cookies import RequestsCookieJar  # For mocking
from requests.structures import CaseInsensitiveDict  # For mocking

from iam_lib.client import Client
from iam_lib.api.access import AccessClient
from iam_lib.api.authorized import AuthorizedClient
from iam_lib.api.eml import EMLClient
from iam_lib.api.resource import ResourceClient
from iam_lib.api.rule import RuleClient
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


@pytest.fixture
def access_client():
    return AccessClient(
        scheme="HTTPS",
        host="localhost",
        accept="JSON",
        public_key_path="./data/public_key.pem",
        algorithm="ES256",
        token=make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    )


@pytest.fixture
def authorized_client():
    return AuthorizedClient(
        scheme="HTTPS",
        host="localhost",
        accept="JSON",
        public_key_path="./data/public_key.pem",
        algorithm="ES256",
        token=make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    )


@pytest.fixture
def eml_client():
    return EMLClient(
        scheme="HTTPS",
        host="localhost",
        accept="JSON",
        public_key_path="./data/public_key.pem",
        algorithm="ES256",
        token=make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    )


@pytest.fixture
def resource_client():
    return ResourceClient(
        scheme="HTTPS",
        host="localhost",
        accept="JSON",
        public_key_path="./data/public_key.pem",
        algorithm="ES256",
        token=make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    )


@pytest.fixture
def rule_client():
    return RuleClient(
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
