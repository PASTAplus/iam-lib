#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    utilities

:Synopsis:
    Pytest utilities

:Author:
    servilla

:Created:
    5/15/25
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path

import daiquiri
import jwt

from tests.config import Config


logger = daiquiri.getLogger(__name__)


def make_token() -> str:
    now = datetime.now(tz=timezone.utc)
    payload = {
        "sub": "EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        "cn": None,
        "email": None,
        "gn": None,
        "hd": "edirepository.org",
        "iss": "https://auth.edirepository.org",
        "sn": None,
        "iat": now,
        "nbf": now,
        "exp": now + timedelta(hours=1),
        "principals": [],
        "isEmailEnabled": False,
        "isEmailVerified": False,
        "identityId": None,
        "idpName": None,
        "idpUid": None,
        "idpCname": None,
    }
    private_key_path = Config.PRIVATE_KEY_PATH
    algorithm = Config.JWT_ALGORITHM
    token = jwt.encode(payload, Path(private_key_path).read_text().encode("utf-8"), algorithm=algorithm)
    return token

