#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_profile_api

:Synopsis:
    Pytest for the profile API

:Author:
    servilla

:Created:
    5/15/25
"""
from unittest.mock import MagicMock

import daiquiri
import requests

from tests.fixtures import profile_client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_create_profile(profile_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'CREATE_PROFILE': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    profile_client.create_profile(
        principal="uid=jack,o=EDI,dc=edirepository,dc=org",
    )
    assert profile_client.response.status_code == 200
    assert profile_client.response.text == "{'CREATE_PROFILE': 'OK'}"


def test_update_profile(profile_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'UPDATE_PROFILE': 'OK'}"
    )
    mocker.patch.object(requests, "put", return_value=mock_requests_response)
    profile_client.update_profile(
        edi_identifier="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        given_name="Jack",
        family_name="Black",
        email="jack.black@email.com"
    )
    assert profile_client.response.status_code == 200
    assert profile_client.response.text == "{'UPDATE_PROFILE': 'OK'}"


def test_delete_profile(profile_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'DELETE_PROFILE': 'OK'}"
    )
    mocker.patch.object(requests, "delete", return_value=mock_requests_response)
    profile_client.delete_profile(
        edi_identifier="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
    )
    assert profile_client.response.status_code == 200
    assert profile_client.response.text == "{'DELETE_PROFILE': 'OK'}"


def test_read_profile(profile_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'READ_PROFILE': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    profile_client.read_profile(
        edi_identifier="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
    )
    assert profile_client.response.status_code == 200
    assert profile_client.response.text == "{'READ_PROFILE': 'OK'}"
