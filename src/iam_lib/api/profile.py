#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    profile

:Synopsis:
    IAM REST API profile client

:Author:
    servilla

:Created:
    5/22/25
"""
import daiquiri

from iam_lib.api.client import Client
import iam_lib.models.response_model as response_model


logger = daiquiri.getLogger(__name__)


class ProfileClient(Client):
    """IAM Profile client class"""

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

    def create_profile(
            self,
            idp_uid: str,
    ) -> str | dict:
        """Create profile.

        Args:
            idp_uid (str): IdP identifier

        Returns:
            Profile identifier (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = "auth/v1/profile"
        form_params = {
            "idp_uid": idp_uid,
        }
        self.post(route=route, form_params=form_params)
        return response_model.response_data(self)


    def update_profile(
        self,
        edi_identifier: str,
        given_name: str,
        family_name: str,
        email: str
    ) -> None:
        """Update profile.

        Args:
            edi_identifier (str): IAM edi identifier
            given_name (str): IAM user given name
            family_name (str): IAM user family name
            email (str): IAM user preferred email

        Returns:
            None

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = f"auth/v1/profile/{edi_identifier}"
        form_params = {
            "given_name": given_name,
            "family_name": family_name,
            "email": email
        }
        self.put(route=route, form_params=form_params)
        return None

    def delete_profile(
        self,
        edi_identifier: str,
    ) -> None:
        """Delete profile.

        Args:
            edi_identifier (str): IAM edi identifier

         Returns:
            None

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = f"auth/v1/profile/{edi_identifier}"
        self.delete(route=route)
        return None

    def read_profile(
        self,
        edi_identifier: str,
    ) -> str | dict:
        """Read profile.

        Args:
            edi_identifier (str): IAM edi identifier

         Returns:
            profile (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/resource/{edi_identifier}"
        self.get(route=route)
        return response_model.response_data(self)
