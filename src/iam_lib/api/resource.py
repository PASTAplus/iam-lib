#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    resource

:Synopsis:
    IAM REST API resource client

:Author:
    servilla

:Created:
    5/13/25
"""
import daiquiri

from iam_lib.client import Client


logger = daiquiri.getLogger(__name__)


def create_resource(
        client: Client,
        resource_key: str,
        resource_label: str,
        resource_type: str,
        parent_resource_key: str = None
) -> None:
    """Create a new resource.

    Args:
        client (iam_lib.client.Client): IAM REST API client
        resource_key (str): unique identifier for the resource
        resource_label (str): human interpretable label of the resource
        resource_type (str): type of resource
        parent_resource_key (str): unique identifier for the parent resource if exists; otherwise None

    Returns:
        None

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
    """
    route = "/auth/v1/resource"
    parameters = {
        "resource_key": resource_key,
        "resource_label": resource_label,
        "resource_type": resource_type,
        "parent_resource_key": parent_resource_key
    }
    client.response = client.post(route=route, parameters=parameters)
    return None


def update_resource(
        client: Client,
        resource_key: str,
        resource_label: str,
        resource_type: str,
        parent_resource_key: str = None
) -> None:
    """Update an existing resource.

    Args:
        client (iam_lib.client.Client): IAM REST API client
        resource_key (str): unique identifier for the resource
        resource_label (str): human interpretable label of the resource
        resource_type (str): type of resource
        parent_resource_key (str): unique identifier for the parent resource if exists; otherwise None

    Returns:
        None

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
    """
    route = f"/auth/v1/resource/{resource_key}"
    parameters = {
        "resource_label": resource_label,
        "resource_type": resource_type,
        "parent_resource_key": parent_resource_key
    }
    client.response = client.put(route=route, parameters=parameters)
    return None


def delete_resource(
        client: Client,
        resource_key: str
) -> None:
    """Delete an existing resource.

    Args:
        client (iam_lib.client.Client): IAM REST API client
        resource_key (str): unique identifier for the resource

     Returns:
        None

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
    """
    route = f"/auth/v1/resource/{resource_key}"
    client.response = client.delete(route=route)
    return None
