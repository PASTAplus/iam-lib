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

from iam_lib.api.client import Client
import iam_lib.models.response_model as response_model


logger = daiquiri.getLogger(__name__)


class RuleClient(Client):
    """IAM Rule client class"""
    
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

    def create_rule(
            self,
            resource_key: str,
            principal: str,
            permission: str
    ) -> None:
        """Create rule.
        Args:
            resource_key (str): unique identifier for the resource
            principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)
            permission (str): IAM permission (read, write, or changePermission)
    
        Returns:
            None
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
    
        """
        route = "auth/v1/rule"
        parameters = {
            "resource_key": resource_key,
            "principal": principal,
            "permission": permission,
        }
        self.post(route=route, form_params=parameters)
        return None
    
    
    def update_rule(
            self,
            resource_key: str,
            principal: str,
            permission: str,
    ) -> None:
        """Update rule.
    
        Args:
            resource_key (str): unique identifier for the resource
            principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)
            permission (str): IAM permission (read, write, or changePermission)
    
        Returns:
            None
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = f"auth/v1/rule/{resource_key}/{principal}"
        parameters = {
            "permission": permission
        }
        self.put(route=route, form_params=parameters)
        return None
    
    
    def delete_rule(
            self,
            resource_key: str,
            principal: str,
    ) -> None:
        """Delete rule.
    
        Args:
            resource_key (str): unique identifier for the resource
            principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)
    
        Returns:
            None
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
        """
        route = f"auth/v1/rule/{resource_key}/{principal}"
        self.delete(route=route)
        return None
    
    
    def read_rule(
            self,
            resource_key: str,
            principal: str,
    ) -> str | dict:
        """Read rule.
    
        Args:
            resource_key (str): unique identifier for the resource
            principal (str): IAM principal (user profile or group EDI-ID or IdP identifier)
    
        Returns:
            rule (str | dict)
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/rule/{resource_key}/{principal}"
        self.get(route=route)
        return response_model.response_data(self)
    
    
    def read_principal_rules(
            self
    ) -> str | dict:
        """Read rules associated with principal who has changePermission.
    
        Args:
            None
    
        Returns:
            rule (str | dict)
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/rules/principal"
        self.get(route=route)
        return response_model.response_data(self)
    
    
    def read_resource_rules(
            self,
            resource_key: str,
    ) -> str | dict:
        """Read rules associated with a resource.
    
        Args:
            resource_key (str): unique identifier for the resource
    
        Returns:
            rule (str | dict)
    
        Raises:
            iam_lib.exceptions.IAMRequestError: On HTTP request error
            iam_lib.exceptions.IAMResponseError: On non-200 response
            iam_lib.exceptions.IAMJSONDecodeError: On JSON decode error
        """
        route = f"auth/v1/rules/resource/{resource_key}"
        self.get(route=route)
        return response_model.response_data(self)
