#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_edi_token_api

:Synopsis:
    Pytest for the EDI Token API

:Author:
    servilla

:Created:
    6/1/25
"""
from unittest.mock import MagicMock

import daiquiri
import requests

from tests.fixtures import edi_token_client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_create_token(edi_token_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"CREATE_TOKEN\": \"OK\"}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    edi_token_client.create_token(
        sub="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
    )
    assert edi_token_client.response.status_code == 200
    assert edi_token_client.response.text == "{\"CREATE_TOKEN\": \"OK\"}"


def test_revoke_token(edi_token_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"REVOKE_TOKEN\": \"OK\"}"
    )
    mocker.patch.object(requests, "put", return_value=mock_requests_response)
    edi_token_client.revoke_token(
        sub="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
    )
    assert edi_token_client.response.status_code == 200
    assert edi_token_client.response.text == "{\"REVOKE_TOKEN\": \"OK\"}"


def test_lock_token(edi_token_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"LOCK_TOKEN\": \"OK\"}"
    )
    mocker.patch.object(requests, "delete", return_value=mock_requests_response)
    edi_token_client.lock_token(
        sub="EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert edi_token_client.response.status_code == 200
    assert edi_token_client.response.text == "{\"LOCK_TOKEN\": \"OK\"}"
