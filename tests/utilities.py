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
from datetime import datetime
from pathlib import Path

import daiquiri
import jwt


logger = daiquiri.getLogger(__name__)


def make_token(exp: datetime) -> str:
    payload = {
        "cn": "jack",
        "email": None,
        "exp": exp,
        "gn": "jack",
        "hd": "edirepository.org",
        "iat": 1746738975,
        "iss": "https://auth.edirepository.org",
        "nbf": 1746738975,
        "pastaGroups": [],
        "pastaIdentityId": 3,
        "pastaIdpName": "ldap",
        "pastaIdpUid":"uid=jack,o=EDI,dc=edirepository,dc=org",
        "pastaIsAuthenticated": True,
        "pastaIsEmailEnabled": False,
        "pastaIsEmailVerified": False,
        "pastaIsVetted": True,
        "sn": None,
        "sub": "EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    }
    private_key_path = "./data/private_key.pem"
    algorithm = "ES256"
    token = jwt.encode(payload, Path(private_key_path).read_text().encode("utf-8"), algorithm=algorithm)
    return token

