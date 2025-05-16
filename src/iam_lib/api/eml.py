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

from iam_lib.client import Client


logger = daiquiri.getLogger(__name__)


def add_eml(
        client: Client,
        principal: str,
        eml: str
) -> None:
    """To parse a valid EML document and add its ACRs to the ACR registry for the resources identified in the EML
    document

    Args:
        client (iam_lib.client.Client): IAM REST API client
        principal (str): IAM principal owner (user profile EDI-ID or IdP identifier)
        eml (str): valid EML document

    Returns:
        None

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
    """
    route = "auth/v1/eml"
    parameters = {
        "principal": principal,
        "eml": eml,
    }
    client.post(route=route, parameters=parameters)
    return None
