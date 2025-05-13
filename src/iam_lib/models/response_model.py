#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    response_model

:Synopsis:
    Converts a IAM HTTP REST API response into an appropriate data structure.

:Author:
    servilla

:Created:
    5/13/25
"""
import json

import daiquiri

import iam_lib
from iam_lib.client import Client
import iam_lib.exceptions


logger = daiquiri.getLogger(__name__)


def response_data(client: Client) -> str | dict:
    """Returns the data structure in a format determined by the accept type

    Args:
        client (iam_lib.client.Client): IAM REST API client

    Returns:
        response_data_structure (str | dict): the data structure

    Raises:
        iam_lib.errors.IAMJSONDecodeError: On invalid JSON

    """
    if client.accept == "JSON":
        try:
            return json.loads(client.response.body)
        except json.decoder.JSONDecodeError as e:
            raise iam_lib.exceptions.IAMJSONDecodeError(e)
    else:
        return client.response.body  # As XML str