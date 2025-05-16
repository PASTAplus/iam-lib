#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_eml_api

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

import iam_lib.api.eml as iam_eml

from fixtures import client, cookies, headers


logger = daiquiri.getLogger(__name__)


def test_add_eml(client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'ADD_EML': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    iam_eml.add_eml(
        client=client,
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        eml="<eml></eml>"
    )
    assert client.response.status_code == 200
    assert client.response.body == "{'ADD_EML': 'OK'}"
