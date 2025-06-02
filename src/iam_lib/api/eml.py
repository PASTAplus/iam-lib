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

from iam_lib.api.client import Client


logger = daiquiri.getLogger(__name__)


class EMLClient(Client):
    """IAM EML client class"""

    def __init__(
            self,
            scheme: str,
            host: str,
            accept: str,
            public_key_path: str,
            algorithm: str,
            token: str,
    ):
        super().__init__(scheme, host, accept, public_key_path, algorithm, token)

    def add_eml(
            self,
            eml: str
    ) -> None:
        """To parse a valid EML document and add its ACRs to the ACR registry for the resources identified in the EML
        document

        Args:
            eml (str): valid EML document

        Returns:
            None

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = "auth/v1/eml"
        form_params = {
            "eml": eml,
        }
        self.post(route=route, form_params=form_params)
        return None
