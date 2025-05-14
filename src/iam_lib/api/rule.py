#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    rule

:Synopsis:
    IAM REST API rule client

:Author:
    servilla

:Created:
    5/13/25
"""
import daiquiri

from iam_lib.client import Client
import iam_lib.models.response_model as response_model


logger = daiquiri.getLogger(__name__)


def create_rule(
        client: Client,
        resource_key: str,
        principal: str,
        permission: str
) -> None:
    """Create rule.
    Args:
        client (iam_lib.client.Client): IAM REST API client
        resource_key (str): unique identifier for the resource
        principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)
        permission (str): IAM permission (read, write, or changePermission)

    Returns:
        None

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response

    """
    route = "/auth/v1/rule"
    parameters = {
        "resource_key": resource_key,
        "principal": principal,
        "permission": permission,
    }
    client.post(route=route, parameters=parameters)
    return None


def update_rule(
        client: Client,
        resource_key: str,
        principal: str,
        permission: str,
) -> None:
    """Update rule.

    Args:
        client (iam_lib.client.Client): IAM REST API client
        resource_key (str): unique identifier for the resource
        principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)
        permission (str): IAM permission (read, write, or changePermission)

    Returns:
        None

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
    """
    route = f"/auth/v1/rule/{resource_key}/{principal}"
    parameters = {
        "permission": permission
    }
    client.put(route=route, parameters=parameters)
    return None


def delete_rule(
        client: Client,
        resource_key: str,
        principal: str,
) -> None:
    """Delete rule.

    Args:
        client (iam_lib.client.Client): IAM REST API client
        resource_key (str): unique identifier for the resource
        principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)

    Returns:
        None

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
    """
    route = f"/auth/v1/rule/{resource_key}/{principal}"
    client.delete(route=route)
    return None


def read_rule(
        client: Client,
        resource_key: str,
        principal: str,
) -> str | dict:
    """Read rule.

    Args:
        client (iam_lib.client.Client): IAM REST API client
        resource_key (str): unique identifier for the resource
        principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)

    Returns:
        rule (str | dict)

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
        iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
    """
    route = f"/auth/v1/rule/{resource_key}/{principal}"
    client.get(route=route)
    return response_model.response_data(client)


def read_principal_rules(
        client: Client,
        principal: str,
) -> str | dict:
    """Read rules associated with principal.

    Args:
        client (iam_lib.client.Client): IAM REST API client
        principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)

    Returns:
        rule (str | dict)

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
        iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
    """
    route = f"/auth/v1/rules/principal/{principal}"
    client.get(route=route)
    return response_model.response_data(client)


def read_resource_rules(
        client: Client,
        resource_key: str,
) -> str | dict:
    """Read rules associated with a resource.

    Args:
        client (iam_lib.client.Client): IAM REST API client
        resource_key (str): unique identifier for the resource

    Returns:
        rule (str | dict)

    Raises:
        iam_lib.exceptions.IAMRequestError: On HTTP request error
        iam_lib.exceptions.IAMResponseError: On non-200 response
        iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
    """
    route = f"/auth/v1/rules/resource_key/{resource_key}"
    client.get(route=route)
    return response_model.response_data(client)
