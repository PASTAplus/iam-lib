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

from tests.fixtures import access_client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_add_access(access_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'ADD_ACCESS': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    access_client.add_access(
        access="<access></access>",
        resource_key="api_service_xyz",
        resource_label="xyz",
        resource_type="service"
    )
    assert access_client.response.status_code == 200
    assert access_client.response.text == "{'ADD_ACCESS': 'OK'}"
