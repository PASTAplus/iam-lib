#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    token

:Synopsis:
    EDI IAM token decoder

: Author:
    servilla

:Created:
    5/10/25
"""
from pathlib import Path

import daiquiri
import jwt

import iam_lib.exceptions

logger = daiquiri.getLogger(__name__)


class Token:
    """EDI IAM JWT token decoder.

    Decodes and validates an EDI IAM JWT token.

    Args:
        token (str): EDI IAM JWT token

    """

    def __init__(self, token: str):
        self.token = token
        self.header = jwt.get_unverified_header(token)
        self.payload = jwt.decode(token,  options={"verify_signature": False})

    @property
    def subject(self) -> str:
        return self.payload.get("sub")

    @property
    def common_name(self) -> str:
        return self.payload.get("cn")

    @property
    def email(self) -> str:
        return self.payload.get("email")

    @property
    def principals(self) -> list:
        return self.payload.get("principals")

    @property
    def is_email_enabled(self) -> bool:
        return self.payload.get("isEmailEnabled")

    @property
    def is_email_verified(self) -> bool:
        return self.payload.get("isEmailVerified")

    @property
    def identity_id(self) -> int:
        return self.payload.get("identityId")

    @property
    def idp_name(self) -> str:
        return self.payload.get("idpName")

    @property
    def idp_uid(self) -> str:
        return self.payload.get("idpUid")

    @property
    def idp_common_name(self) -> str:
        return self.payload.get("idpCName")

    @property
    def issuer(self) -> str:
        return self.header.get("iss")

    @property
    def hosted_domain(self) -> str:
        return self.header.get("hd")

    @property
    def issued_at(self) -> int:
        return self.payload.get("iat")

    @property
    def not_before(self) -> int:
        return self.payload.get("nbf")

    @property
    def expiry(self) -> int:
        return self.payload.get("exp")

    @property
    def links(self) -> list:
        return self.payload.get("links")

    def validate(self, public_key_path: str, algorithm: str):
        """Validate EDI token

            public_key (str): Public key
            algorithm (str): Digital signing-algorithm
        """
        with open(Path(public_key_path), "r") as f:
            public_key_text = f.read()
            public_key = public_key_text.encode("utf-8")
        try:
            jwt.decode(self.token, public_key, algorithms=[algorithm])
        except jwt.InvalidTokenError as e:
            raise iam_lib.exceptions.IAMInvalidToken(f"Invalid token: {e}")
