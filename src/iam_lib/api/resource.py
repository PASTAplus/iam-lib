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

from iam_lib.api.client import Client
import iam_lib.models.response_model as response_model

logger = daiquiri.getLogger(__name__)


class ResourceClient(Client):
    """IAM Resource client class"""

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

    def create_resource(
        self,
        resource_key: str,
        resource_label: str,
        resource_type: str,
        parent_resource_key: str = None
    ) -> None:
        """Create resource.

        Args:
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
        route = "auth/v1/resource"
        form_params = {
            "resource_key": resource_key,
            "resource_label": resource_label,
            "resource_type": resource_type,
            "parent_resource_key": parent_resource_key
        }
        self.post(route=route, form_params=form_params)
        return None

    def update_resource(
        self,
        resource_key: str,
        resource_label: str,
        resource_type: str,
        parent_resource_key: str = None
    ) -> None:
        """Update resource.

        Args:
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
        route = f"auth/v1/resource/{resource_key}"
        form_params = {
            "resource_label": resource_label,
            "resource_type": resource_type,
            "parent_resource_key": parent_resource_key
        }
        self.put(route=route, form_params=form_params)
        return None

    def delete_resource(
        self,
        resource_key: str
    ) -> None:
        """Delete resource.

        Args:
            resource_key (str): unique identifier for the resource

         Returns:
            None

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = f"auth/v1/resource/{resource_key}"
        self.delete(route=route)
        return None

    def read_resource(
        self,
        resource_key: str,
        descendants: bool = False,
        ancestors: bool = False,
        all: bool = False
    ) -> str | dict:
        """Read resource (optional tree).

        Args:
            resource_key (str): unique identifier for the resource
            descendants (bool): include resource descendants (optional)
            ancestors (bool): include resource ancestors (optional)
            all (bool): include all resources (optional)

         Returns:
            resource_tree (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/resource/{resource_key}"
        query_params = {}
        if descendants or ancestors or all:
            if descendants: query_params["descendants"] = None
            if ancestors: query_params["ancestors"] = None
            if all: query_params["all"] = None
        self.get(route=route, query_params=query_params)
        return response_model.response_data(self)

    def read_resources(
        self,
    ) -> str | dict:
        """Read resources of EDI Token subject.

        Args:
            None

         Returns:
            resources (str | dict)

        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/resources"
        self.get(route=route)
        return response_model.response_data(self)
