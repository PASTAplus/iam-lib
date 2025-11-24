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
import pytest
from requests.cookies import RequestsCookieJar  # For mocking
from requests.structures import CaseInsensitiveDict  # For mocking

from iam_lib.api.client import Client
from iam_lib.api.access import AccessClient
from iam_lib.api.authorized import AuthorizedClient
from iam_lib.api.edi_token import EdiTokenClient
from iam_lib.api.eml import EMLClient
from iam_lib.api.profile import ProfileClient
from iam_lib.api.resource import ResourceClient
from iam_lib.api.rule import RuleClient
from tests.config import Config
from tests.utilities import make_token


TOKEN = make_token("EDI-221c782cc3c84fcba888fadd7cbe708a")


@pytest.fixture(scope="function")
def client():
    return Client(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=TOKEN
    )


@pytest.fixture
def access_client():
    return AccessClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=TOKEN
    )


@pytest.fixture
def authorized_client():
    return AuthorizedClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=TOKEN
    )


@pytest.fixture
def edi_token_client():
    return EdiTokenClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=TOKEN
    )


@pytest.fixture
def eml_client():
    return EMLClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=TOKEN
    )


@pytest.fixture
def profile_client():
    return ProfileClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=TOKEN
    )


@pytest.fixture
def resource_client():
    return ResourceClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=TOKEN
    )


@pytest.fixture
def rule_client():
    return RuleClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=TOKEN
    )


@pytest.fixture(scope="function")
def cookies():
    cookies = RequestsCookieJar()
    cookies.set(
        name="pasta_token",
        value=f"{TOKEN}",
        domain="edirepository.org"
    )
    return cookies


@pytest.fixture(scope="function")
def headers():
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    return headers
