#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    token

:Synopsis:
    Perform EDI IAM authentication token validation
:Author:
    servilla

:Created:
    5/10/25
"""
from pathlib import Path

import daiquiri
import jwt

import iam_lib.exceptions

logger = daiquiri.getLogger(__name__)


def validate(token: str, public_key: bytes, algorithm: str):
    """Validate EDI token

        token (str): EDI IAM JWT token
        public_key (bytes): Public key
        algorithm (str): Digital signing-algorithm
    """
    try:
        jwt.decode(token, public_key, algorithms=algorithm)
    except jwt.InvalidTokenError as e:
        raise iam_lib.exceptions.IAMInvalidToken(f"Invalid token: {e}")
    return token
