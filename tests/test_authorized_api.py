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


logger = daiquiri.getLogger(__name__)


def test_is_authorized(authorized_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"IS_AUTHORIZED\": \"OK\"}"
    )
    mocker.patch.object(requests, "get", return_value=mock_requests_response)
    is_authorized = authorized_client.is_authorized(
        resource_key="resource_xyz",
        permission="write"
    )
    assert is_authorized is True
    assert authorized_client.response.status_code == 200
    assert authorized_client.response.text == "{\"IS_AUTHORIZED\": \"OK\"}"
