#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    edi_token

:Synopsis:
    IAM REST API edi_token client

:Author:
    servilla

:Created:
    6/1/25
"""
import daiquiri

from iam_lib.api.client import Client
import iam_lib.models.response_model as response_model

logger = daiquiri.getLogger(__name__)


class EdiTokenClient(Client):
    """IAM EDI Token client class"""

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

    def create_token(
        self,
        profile_edi_identifier: str,
        key: str
    ) -> str | dict:
        """Create token. Returns an EDI IAM JWT base64 digitally signed token.
        Args:
            profile_edi_identifier (str): Profile IAM edi identifier
            key (str): authentication key

        Returns:
            Response object (str | dict)
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/token/{profile_edi_identifier}"
        form_params = {
            "key": key,
        }
        self.post(route=route, form_params=form_params)
        return response_model.response_data(self)

    def lock_token(
        self,
        profile_edi_identifier: str
    ) -> str | dict:
        """Lock tokens from being created.

        Args:
            profile_edi_identifier (str): Profile IAM edi identifier

        Returns:
            None

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/token/{profile_edi_identifier}"
        self.delete(route=route)
        return response_model.response_data(self)

    def refresh_token(self,
      auth_token: str,
      edi_token: str
    ) -> str | dict:
        """Refresh token(s). Given a valid token pair (auth_token, edi_token), request a new token pair.

        Args:
            auth_token (str): PASTA authentication token
            edi_token (str): IAM edi token

        Returns:
            Response object (str | dict)

        Raise:

        """
        route = "auth/v1/refresh"
        form_params = {
            "pasta-token": auth_token,
            "edi-token": edi_token
        }
        self.post(route=route,  form_params=form_params)
        return response_model.response_data(self)

    def revoke_token(
        self,
        profile_edi_identifier: str
    ) -> str | dict:
        """Revoke token.
    
        Args:
            profile_edi_identifier (str): Profile IAM edi identifier

        Returns:
            Response object (str | dict)
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/token/{profile_edi_identifier}"
        self.put(route=route)
        return response_model.response_data(self)

