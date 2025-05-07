"""
:Mod: test_requests_wrapper

:Synopsis:
    Pytest for test_requests_wrapper

:Author:
    Mark Servilla

:Created:
    2025-05-05

"""
import pytest

from iam_lib.requests_wrapper import RequestsWrapper

@pytest.fixture()
def requests_data():
    requests_data = {}
    requests_data["verb"] = "GET"
    requests_data["url"] = "https://auth.edirepository.org/ping"
    requests_data["token"] = "some_client_token"
    requests_data["accept"] = "json"
    requests_data["kwargs"] = {
        "token": "some_on_behalf_token",
        "resource_key": "https://pasta.lternet.edu/package/eml/edi/1/1",
        "principal": "edi-090989243203409",
        "permission": "read"
    }
    return requests_data

def test_requests_wrapper(requests_data):
    rw = RequestsWrapper(
        requests_data["verb"],
        requests_data["url"],
        requests_data["token"],
        requests_data["accept"],
        requests_data["kwargs"]
    )

