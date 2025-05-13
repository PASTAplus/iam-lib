#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    eml

:Synopsis:
    IAM REST API eml client

:Author:
    servilla

:Created:
    5/11/25
"""
import daiquiri

from iam_lib.response import Response
from iam_lib.client import Client


logger = daiquiri.getLogger(__name__)


def add_eml(client: Client, principal: str, eml: str):
    """To parse a valid EML document and add its ACRs to the ACR registry for the resources identified in the EML
    document

    Args:
        client (iam_lib.client.Client): IAM REST API client
        token (str): IAM JWT token
        principal (str): IAM principal owner (either EDI-ID or IdP identifier)
        eml (str): EML document

    Returns:
        None

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
    """
    route = "/auth/v1/eml"
    body = {
        "principal": principal,
        "eml": eml,
    }
    return client.post(route=route, body=body)
