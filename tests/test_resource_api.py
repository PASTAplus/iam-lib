#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_resource_api

:Synopsis:
    Pytest for the resource API

:Author:
    servilla

:Created:
    5/15/25
"""
from unittest.mock import MagicMock

import daiquiri
import requests

from tests.fixtures import resource_client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_create_resource(resource_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'CREATE_RESOURCE': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    resource_client.create_resource(
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        resource_key="resource_xyz",
        resource_label="xyz",
        resource_type="resource"
    )
    assert resource_client.response.status_code == 200
    assert resource_client.response.body == "{'CREATE_RESOURCE': 'OK'}"


def test_update_resource(resource_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'UPDATE_RESOURCE': 'OK'}"
    )
    mocker.patch.object(requests, "put", return_value=mock_requests_response)
    resource_client.update_resource(
        resource_key="resource_xyz",
        resource_label="xyz",
        resource_type="resource",
        parent_resource_key="parent_resource_xyz"
    )
    assert resource_client.response.status_code == 200
    assert resource_client.response.body == "{'UPDATE_RESOURCE': 'OK'}"


def test_delete_resource(resource_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'DELETE_RESOURCE': 'OK'}"
    )
    mocker.patch.object(requests, "delete", return_value=mock_requests_response)
    resource_client.delete_resource(
        resource_key="resource_xyz"
    )
    assert resource_client.response.status_code == 200
    assert resource_client.response.body == "{'DELETE_RESOURCE': 'OK'}"


def test_read_resource(resource_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'READ_RESOURCE': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    resource_client.read_resource(
        resource_key="resource_xyz",
        ancestors=True,
        all=True
    )
    assert resource_client.response.status_code == 200
    assert resource_client.response.body == "{'READ_RESOURCE': 'OK'}"


def test_read_resources(resource_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'READ_RESOURCES': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    resource_client.read_resources(
        principal = "EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert resource_client.response.status_code == 200
    assert resource_client.response.body == "{'READ_RESOURCES': 'OK'}"


