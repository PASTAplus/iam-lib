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

from iam_lib.api.client import Client
from iam_lib.exceptions import IAMResponseError

logger = daiquiri.getLogger(__name__)


class AuthorizedClient(Client):
    """IAM Authorized client class"""

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

    def is_authorized(
            self,
            resource_key: str,
            permission: str
    ) -> bool:
        """Test if principal as identified in the authentication token is authorized to access the resource at the
        given permission

        Args:
            resource_key (str): unique identifier for the resource
            permission (str): IAM permission (read, write, or changePermission)

        Returns:
            Boolean: True if the principal is authorized to access the resource

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
        """
        query_params = {
            "resource_key": resource_key,
            "permission": permission,
        }
        route = f"auth/v1/authorized"
        try:
            self.get(route=route, query_params=query_params)
            return True
        except IAMResponseError as e:
            logger.error(e)
            return False

