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

from tests.fixtures import (
    cookies,
    eml_client,
    headers
)


logger = daiquiri.getLogger(__name__)


def test_add_eml(eml_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{'ADD_EML': 'OK'}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    eml_client.add_eml(
        eml="<eml></eml>"
    )
    assert eml_client.response.status_code == 200
    assert eml_client.response.text == "{'ADD_EML': 'OK'}"
