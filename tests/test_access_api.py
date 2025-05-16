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

import iam_lib.api.access as iam_access

from fixtures import client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_add_access(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'ADD_ACCESS': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    iam_access.add_access(
        client=client,
        access="<access></access>",
        resource_key="api_service_xyz",
        resource_label="xyz",
        resource_type="service"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'ADD_ACCESS': 'OK'}"
