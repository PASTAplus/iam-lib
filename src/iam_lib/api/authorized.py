#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    authorized

:Synopsis:
    IAM REST API authorization client

:Author:
    servilla

:Created:
    5/13/25
"""
import daiquiri

from iam_lib.client import Client
from iam_lib.exceptions import IAMRequestError, IAMResponseError

logger = daiquiri.getLogger(__name__)


def is_authorized(
        client: Client,
        token: str,
        resource_key: str,
        permission: str
) -> bool:
    """Test if principal is authorized to access the resource at the given permission

    Args:
        client (iam_lib.client.Client): IAM REST API client
        token (str): IAM user JWT token
        resource_key (str): unique identifier for the resource
        permission (str): IAM permission (read, write, or changePermission)

    Returns:
        Boolean: True if the principal is authorized to access the resource
    """
    route = "/auth/v1/authorized"
    parameters = {
        "token": token,
        "resource_key": resource_key,
        "permission": permission
    }
    try:
        client.post(route=route, parameters=parameters)
        return True
    except (IAMRequestError, IAMResponseError) as e:
        logger.error(e)
        return False
