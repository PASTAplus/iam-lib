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

from iam_lib.models.permission import Permission, PERMISSION_MAP
from tests.conftest import rule_client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_create_rule(rule_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"CREATE_RULE\": \"OK\"}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    rule_client.create_rule(
        resource_key="resource_xyz",
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        permission=Permission(PERMISSION_MAP.index("write"))
    )
    assert rule_client.response.status_code == 200
    assert rule_client.response.text == "{\"CREATE_RULE\": \"OK\"}"


def test_update_rule(rule_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"UPDATE_RULE\": \"OK\"}"
    )
    mocker.patch.object(requests, "put", return_value=mock_requests_response)
    rule_client.update_rule(
        resource_key="resource_xyz",
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        permission=Permission(PERMISSION_MAP.index("write"))
    )
    assert rule_client.response.status_code == 200
    assert rule_client.response.text == "{\"UPDATE_RULE\": \"OK\"}"


def test_delete_rule(rule_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"DELETE_RULE\": \"OK\"}"
    )
    mocker.patch.object(requests, "delete", return_value=mock_requests_response)
    rule_client.delete_rule(
        resource_key="resource_xyz",
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert rule_client.response.status_code == 200
    assert rule_client.response.text == "{\"DELETE_RULE\": \"OK\"}"


def test_read_rule(rule_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"READ_RULE\": \"OK\"}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    rule_client.read_rule(
        resource_key="resource_xyz",
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert rule_client.response.status_code == 200
    assert rule_client.response.text == "{\"READ_RULE\": \"OK\"}"


def test_read_principal_rules(rule_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"READ_PRINCIPAL_RULES\": \"OK\"}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    rule_client.read_principal_rules()
    assert rule_client.response.status_code == 200
    assert rule_client.response.text == "{\"READ_PRINCIPAL_RULES\": \"OK\"}"


def test_read_resource_rules(rule_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"READ_RESOURCE_RULES\": \"OK\"}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    rule_client.read_resource_rules(
        resource_key="resource_xyz",
    )
    assert rule_client.response.status_code == 200
    assert rule_client.response.text == "{\"READ_RESOURCE_RULES\": \"OK\"}"

