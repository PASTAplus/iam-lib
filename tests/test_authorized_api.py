#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_authorized_api

:Synopsis:
    Pytest for the authorized API

:Author:
    servilla

:Created:
    5/15/25
"""
from unittest.mock import MagicMock

import daiquiri
import requests

import iam_lib.api.authorized as iam_authorized

from fixtures import client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_is_authorized(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'IS_AUTHORIZED': 'OK'}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    is_authorized = iam_authorized.is_authorized(
        client=client,
        token=client.token,
        resource_key="resource_xyz",
        permission="write"
    )
    assert is_authorized is True
    assert client.response.status_code == 200
    assert client.response.body == "{'IS_AUTHORIZED': 'OK'}"
