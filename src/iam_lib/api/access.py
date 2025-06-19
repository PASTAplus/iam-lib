#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    access

:Synopsis:
    IAM REST API access element client

:Author:
    servilla

:Created:
    5/13/25
"""
import daiquiri

from iam_lib.api.client import Client


logger = daiquiri.getLogger(__name__)


class AccessClient(Client):
    """IAM Access Client class"""

    def __init__(
            self,
            scheme: str,
            host: str,
            accept: str,
            public_key_path: str,
            algorithm: str,
            token: str,
            truststore: str = None,
    ):
        super().__init__(scheme, host, accept, public_key_path, algorithm, token, truststore)


    def add_access(
            self,
            access: str,
            resource_key: str,
            resource_label: str,
            resource_type: str
    ) -> None:
        """To parse a valid EML access element and add its ACRs to the ACR registry for the resource identified by
        the resource key.

        Args:
            access (str): valid EML access element
            resource_key (str): unique identifier for the resource
            resource_label (str): human interpretable label of the resource
            resource_type (str): type of resource

        Returns:
            None

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = "auth/v1/access"
        form_params = {
            "access": access,
            "resource_key": resource_key,
            "resource_label": resource_label,
            "resource_type": resource_type,
        }
        self.post(route=route, form_params=form_params)
        return None
