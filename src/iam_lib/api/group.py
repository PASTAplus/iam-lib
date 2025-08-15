#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    group

:Synopsis:
    IAM REST API group client

:Author:
    servilla

:Created:
    8/15/25
"""
import daiquiri

from iam_lib.api.client import Client
import iam_lib.models.response_model as response_model

logger = daiquiri.getLogger(__name__)


class GroupClient(Client):
    """IAM Group client class"""

    def __init__(
        self,
        scheme: str,
        host: str,
        accept: str,
        public_key_path: str,
        algorithm: str,
        token: str,
        truststore: str = None,
        timeout: int = 10,
    ):
        super().__init__(scheme, host, accept, public_key_path, algorithm, token, truststore, timeout)

    def create_group(
        self,
        group_name: str,
        group_description: str = None
    ) -> str | dict:
        """Create group. Return a new group edi identifier.

        Args:
            group_name (str): the visible name of the group
            group_description (str): an optional description of the group

        Returns:
            Response object (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = "auth/v1/group"
        form_params = {
            "group_name": group_name,
            "group_description": group_description,
        }
        self.post(route=route, form_params=form_params)
        return response_model.response_data(self)

    def read_group(
        self,
        group_edi_identifier: str,
    ) -> str | dict:
        """Read group. Returns list of group members.

        Args:
            group_edi_identifier (str): Group IAM edi identifier

        Returns:
            Response object (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/group/{group_edi_identifier}"
        form_params = None
        self.put(route=route, form_params=form_params)
        return response_model.response_data(self)

    def update_group(
        self,
        group_edi_identifier: str,
        group_name: str,
        group_description: str = None
    ) -> str | dict:
        """Update group. Updates group details.

        Args:
            group_edi_identifier (str): Group IAM edi identifier
            group_name (str): the visible name of the group
            group_description (str): an optional description of the group

        Returns:
            Response object (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/group/{group_edi_identifier}"
        form_params = {
            "group_name": group_name,
            "group_description": group_description,
        }
        self.put(route=route, form_params=form_params)
        return response_model.response_data(self)

    def delete_group(
        self,
        group_edi_identifier: str
    ) -> str | dict:
        """Delete group. Removes group from IAM.

        Args:
            group_edi_identifier (str): Group IAM edi identifier

         Returns:
            Response object (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/group/{group_edi_identifier}"
        self.delete(route=route)
        return response_model.response_data(self)

    def add_group_member(
        self,
        group_edi_identifier: str,
        profile_edi_identifier: str
    ) -> str | dict:
        """Add group member. Adds a member to a group.

        Args:
            group_edi_identifier (str): Group IAM edi identifier
            profile_edi_identifier (str): Profile IAM edi identifier

        Returns:
            Response object (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/group/{group_edi_identifier}/{profile_edi_identifier}"
        self.post(route=route)
        return response_model.response_data(self)

    def remove_group_member(
        self,
        group_edi_identifier: str,
        profile_edi_identifier: str
    ) -> str | dict:
        """Remove group member. Removes a member to a group.

        Args:
            group_edi_identifier (str): Group IAM edi identifier
            profile_edi_identifier (str): Profile IAM edi identifier

        Returns:
            Response object (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/group/{group_edi_identifier}/{profile_edi_identifier}"
        self.delete(route=route)
        return response_model.response_data(self)
