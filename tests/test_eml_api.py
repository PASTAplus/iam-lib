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

from fixtures import (
    cookies,
    emlclient,
    headers
)


logger = daiquiri.getLogger(__name__)


def test_add_eml(emlclient, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'ADD_EML': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    emlclient.add_eml(
        principal="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        eml="<eml></eml>"
    )
    assert emlclient.response.status_code == 200
    assert emlclient.response.body == "{'ADD_EML': 'OK'}"
