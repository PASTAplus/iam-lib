#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_rule_api

:Synopsis:
    Pytest for the rules API

:Author:
    servilla

:Created:
    5/15/25
"""
from unittest.mock import MagicMock

import daiquiri
import requests

import iam_lib.api.rule as iam_rule

from fixtures import client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_create_rule(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'CREATE_RULE': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    iam_rule.create_rule(
        client=client,
        resource_key="resource_xyz",
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        permission="write"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'CREATE_RULE': 'OK'}"


def test_update_rule(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'UPDATE_RULE': 'OK'}"
    )
    mocker.patch.object(requests, "put", return_value=mock_requests_response)
    iam_rule.update_rule(
        client=client,
        resource_key="resource_xyz",
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        permission="write"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'UPDATE_RULE': 'OK'}"


def test_delete_rule(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'DELETE_RULE': 'OK'}"
    )
    mocker.patch.object(requests, "delete", return_value=mock_requests_response)
    iam_rule.delete_rule(
        client=client,
        resource_key="resource_xyz",
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'DELETE_RULE': 'OK'}"


def test_read_rule(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'READ_RULE': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    iam_rule.read_rule(
        client=client,
        resource_key="resource_xyz",
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'READ_RULE': 'OK'}"


def test_read_principal_rules(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'READ_PRINCIPAL_RULES': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    iam_rule.read_principal_rules(
        client=client,
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'READ_PRINCIPAL_RULES': 'OK'}"


def test_read_resource_rules(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'READ_RESOURCE_RULES': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    iam_rule.read_resource_rules(
        client=client,
        resource_key="resource_xyz",
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'READ_RESOURCE_RULES': 'OK'}"

