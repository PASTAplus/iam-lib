#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    api_key

:Synopsis:
    IAM REST API api_key client

:Author:
    servilla

:Created:
    6/1/25
"""
import daiquiri

from iam_lib.api.client import Client
import iam_lib.models.response_model as response_model

logger = daiquiri.getLogger(__name__)


class ApiKeyClient(Client):
    """IAM Api Key client class"""

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

    def key_to_token(
        self,
        key: str
    ) -> str | dict:
        """API key to token. Returns an EDI IAM JWT base64 digitally signed token.
        Args:
            key (str): authentication key

        Returns:
            Response object (str | dict)
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/key"
        form_params = {
            "key": key,
        }
        self.post(route=route, form_params=form_params)
        return response_model.response_data(self)
