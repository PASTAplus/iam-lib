"""
:Mod: test_requests_wrapper

:Synopsis:
    Pytest for test_requests_wrapper

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt
import pytest

from iam_lib.requests_wrapper import RequestsWrapper


public_key = Path("./data/public_key.pem").read_text().encode("utf-8")
private_key = Path("./data/private_key.pem").read_text().encode("utf-8")
algorithm = "ES256"


def test_requests_wrapper_init():
    """ Test the initialization of the RequestsWrapper class.
        verb (str): HTTP verb to use
        scheme (str): protocol scheme (http or https)
        host (str): network host domain or address
        token (str): Base64 encoded JWT token of user making request
        accept (str): Accept type either JSON or XML
    """
    token = _make_token(datetime.now(tz=timezone.utc) + timedelta(hours=1))
    rw = RequestsWrapper(
        verb="GET",
        scheme="https",
        host="localhost",
        token=token,
        public_key=public_key,
        algorithm=algorithm,
        accept="JSON"
    )

    assert rw


def _make_token(exp: datetime) -> str:
    payload = {
        'cn': 'jack',
        'email': None,
        'exp': exp,
        'gn': 'jack',
        'hd': 'edirepository.org',
        'iat': 1746738975,
        'iss': 'https://auth.edirepository.org',
        'nbf': 1746738975,
        'pastaGroups': [],
        'pastaIdentityId': 3,
        'pastaIdpName': 'ldap',
        'pastaIdpUid':'uid=jack,o=EDI,dc=edirepository,dc=org',
        'pastaIsAuthenticated': True,
        'pastaIsEmailEnabled': False,
        'pastaIsEmailVerified': False,
        'pastaIsVetted': True,
        'sn': None,
        'sub': 'EDI-3fa734a7cd6e40998a5c2b5486b6eced'
    }

    token = jwt.encode(payload, private_key, algorithm=algorithm)

    return token

