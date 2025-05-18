#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_eml

:Synopsis:
    Pytest for the EML API

:Author:
    servilla

:Created:
    5/15/25
"""
from unittest.mock import MagicMock

import daiquiri
import requests

import iam_lib.api.resource as iam_resource

from fixtures import client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_create_resource(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'CREATE_RESOURCE': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    iam_resource.create_resource(
        client=client,
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        resource_key="resource_xyz",
        resource_label="xyz",
        resource_type="resource"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'CREATE_RESOURCE': 'OK'}"


def test_update_resource(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'UPDATE_RESOURCE': 'OK'}"
    )
    mocker.patch.object(requests, "put", return_value=mock_requests_response)
    iam_resource.update_resource(
        client=client,
        resource_key="resource_xyz",
        resource_label="xyz",
        resource_type="resource",
        parent_resource_key="parent_resource_xyz"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'UPDATE_RESOURCE': 'OK'}"


def test_delete_resource(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'DELETE_RESOURCE': 'OK'}"
    )
    mocker.patch.object(requests, "delete", return_value=mock_requests_response)
    iam_resource.delete_resource(
        client=client,
        resource_key="resource_xyz"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'DELETE_RESOURCE': 'OK'}"


def test_read_resource(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'READ_RESOURCE': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    iam_resource.read_resource(
        client=client,
        resource_key="resource_xyz",
        ancestors=True,
        all=True
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'READ_RESOURCE': 'OK'}"


def test_read_resources(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'READ_RESOURCES': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    iam_resource.read_resources(
        client=client,
        principal = "EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'READ_RESOURCES': 'OK'}"


