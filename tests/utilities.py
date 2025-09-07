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


def make_token(sub: str) -> str:
    now = datetime.now(tz=timezone.utc)
    payload = {
        "sub": f"{sub}",
        "cn": None,
        "email": None,
        "hd": "edirepository.org",
        "iss": "https://auth.edirepository.org",
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

