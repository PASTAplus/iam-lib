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
        sub: str,
    ) -> str:
        """Create token.
        Args:
            sub (str): subject's unique EDI profile identifier

        Returns:
            edi_token (str): JWT base64 digitally signed token
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
    
        """
        route = "auth/v1/token"
        form_params = {
            "sub": sub,
        }
        self.post(route=route, form_params=form_params)
        return response_model.response_data(self)

    def revoke_token(
        self,
        sub: str
    ) -> None:
        """Revoke token.
    
        Args:
            sub (str): subject's unique EDI profile identifier

        Returns:
            None
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = f"auth/v1/token/{sub}"
        self.put(route=route)
        return None

    def lock_token(
        self,
        sub: str
    ) -> None:
        """Lock tokens from being created.
    
        Args:
            sub (str): subject's unique EDI profile identifier
    
        Returns:
            None
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = f"auth/v1/token/{sub}"
        self.delete(route=route)
        return None
