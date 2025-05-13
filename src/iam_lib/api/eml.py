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


def add_eml(client: Client, accept: str, token: str, principal: str, eml: str) -> Response:
    """To parse a valid EML document and add its ACRs to the ACR registry for the resources identified in the EML
    document

    Args:
        client (iam_lib.client.Client): IAM REST API client
        accept (str): Accept format (either JSON or XML)
        token (str): IAM JWT token
        principal (str): IAM principal owner (either EDI-ID or IdP identifier)
        eml (str): EML document

    Returns:
        iam_lib.response.Response: Response object

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
    """
    route = "/auth/v1/eml"
    kwargs = {
        "principal": principal,
        "eml": eml,
    }
    return client.post(token=token, route=route, kwargs=kwargs, accept=accept)
