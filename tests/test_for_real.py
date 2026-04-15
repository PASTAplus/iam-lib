"""
:Mod: client

:Synopsis:
    Tests for real scenarios

:Author:
    Mark Servilla

:Created:
    2025-06-22

"""
import uuid

from iam_lib.token import Token
from iam_lib.api.api_key import ApiKeyClient
from iam_lib.api.edi_token import EdiTokenClient
from iam_lib.api.profile import ProfileClient
from iam_lib.api.resource import ResourceClient
from iam_lib.api.rule import RuleClient
from iam_lib.models.permission import Permission
from tests.config import Config
from tests.utilities import make_token


def test_create_data_package():
    client_token = make_token("EDI-376d4d3e43554771a1dd0a0c52050508")
    profile_client = ProfileClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=client_token,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    idp_uid = "mark.servilla@gmail.com"
    profile_response = profile_client.create_profile(idp_uid=idp_uid)
    print(f"*** {idp_uid} ***")
    response_printer(profile_response)
    EDI_ID = profile_response["edi_id"]
    user_token = make_token(EDI_ID)

    resource_client = ResourceClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=user_token,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    resource_client.create_resource(
        resource_key="http://localhost:8088/package/eml/edi/1790/1",
        resource_label="edi.1790.1",
        resource_type="package",
        parent_resource_key = None
    )

    metadata_collection_key = uuid.uuid4().hex
    resource_client.create_resource(
        resource_key = metadata_collection_key,
        resource_label = "Metadata",
        resource_type = "collection",
        parent_resource_key = "http://localhost:8088/package/eml/edi/1790/1"
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/metadata/eml/edi/1790/1",
        resource_label = "EML Metadata",
        resource_type = "metadata",
        parent_resource_key = metadata_collection_key
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/report/eml/edi/1790/1",
        resource_label = "Quality Report",
        resource_type = "report",
        parent_resource_key = metadata_collection_key
    )

    data_collection_key = uuid.uuid4().hex
    resource_client.create_resource(
        resource_key = data_collection_key,
        resource_label = "Data",
        resource_type = "collection",
        parent_resource_key = "http://localhost:8088/package/eml/edi/1790/1"
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/data/eml/edi/1790/1/e64ec185b099968d9ae653d620e23d31",
        resource_label = "ER_contour",
        resource_type = "data",
        parent_resource_key = data_collection_key
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/data/eml/edi/1790/1/0def6dc28228813fe1c2c28b8cc8d75d",
        resource_label = "Infiltration rate",
        resource_type = "data",
        parent_resource_key = data_collection_key
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/data/eml/edi/1790/1/b6505c7e26a8bc89d0b367bce67b9189",
        resource_label = "Vegetation biomass",
        resource_type = "data",
        parent_resource_key = data_collection_key
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/data/eml/edi/1790/1/6292fea48cc177b8bde77da7be2e3c51",
        resource_label = "treatment",
        resource_type = "data",
        parent_resource_key = data_collection_key
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/data/eml/edi/1790/1/a899574b1de74315526613d9f980019f",
        resource_label = "slake",
        resource_type = "data",
        parent_resource_key = data_collection_key
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/data/eml/edi/1790/1/edb5c9ca550c8142cfa05e0e27af3afd",
        resource_label = "veg_com",
        resource_type = "data",
        parent_resource_key = data_collection_key
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/data/eml/edi/1790/1/8604aecae9ee64a74c52d4c1965bb0ef",
        resource_label = "bare",
        resource_type = "data",
        parent_resource_key = data_collection_key
    )

    resource_client.create_resource(
        resource_key = "http://localhost:8088/package/data/eml/edi/1790/1/4783f2527df74967faaba962c767ccc6",
        resource_label = "soilC",
        resource_type = "data",
        parent_resource_key = data_collection_key
    )

    rule_client = RuleClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=user_token,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    rule_client.create_rule(
        resource_key="http://localhost:8088/package/eml/edi/1790/1",
        principal="EDI-b2757fee12634ccca40d2d689f5c0543",
        permission=Permission.READ,
    )

def test_refresh_token():
    client_token = make_token(Config.AUTH_SERVICE_ID)
    edi_token_client = EdiTokenClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=client_token,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    auth_token = "dWlkPW1zZXJ2aWxsYSxvPUVESSxkYz1lZGlyZXBvc2l0b3J5LGRjPW9yZypodHRwczovL3Bhc3RhLmVkaXJlcG9zaXRvcnkub3JnL2F1dGhlbnRpY2F0aW9uKjE3NTc4MTE0MTM5MzMqdmV0dGVkKmF1dGhlbnRpY2F0ZWQ=-mzxMhqRzHNdPxsjnBUj4syn+zFPETvSwUn7CyjyJsd0I+sAF5vVGiHgQIrVMDg8Z3LkSsLQtRgwtik/Bx60rNCtzcu6APNuJoRqNYLLTu7CCWL2J+RaLGm64u0Lefg6zqQ1BkpJEe5AXTlSjDKYZwvPNvWzCphH1MtH8DYB25jcf8cY6kiNB86f8R2+925Ptoq8ONWdytiF6wgPyqCoZVvNrTGYD9oqkipNfIicw44v3o1IfcEEFb3Itv7J91ExQrJI6V2U2eHQi6ImnaBy4InD7p5gwaitnQ2nCO8uz5X10Gl0gQV8jbg88xCrcdPvUXQqPY6NMGR6rIRZq1NIsVQ=="
    edi_token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJFREktMmY4YTIyODc4ZDMzN2UwOWRkYWJhMTVlZTBlZWU5YmIyOTMzZmQ1NCIsImNuIjoibXNlcnZpbGxhIiwiZW1haWwiOm51bGwsImF2YXRhclVybCI6Imh0dHBzOi8vbG9jYWxob3N0OjU0NDMvYXV0aC91aS9hcGkvYXZhdGFyL2dlbi9NIiwicHJpbmNpcGFscyI6WyJFREktMDc4ZTZlM2NlZTRmN2YyODEyZjE1MDcwMWRhOTM1MWFjYjUxZTA4OSIsIkVESS03YmUzNTEwZDA4ZGVmMGRmYzY2NzgyNGViZDRmNGYxYmJkNzcwMjM0IiwiRURJLWJkYWU3NDk3MmVkNzEwYzU2YjFlMGRmMThjY2I2ZTIzYzMxZjYwZjYiXSwibGlua3MiOltdLCJpc0VtYWlsRW5hYmxlZCI6ZmFsc2UsImlzRW1haWxWZXJpZmllZCI6ZmFsc2UsImlkcENvbW1vbk5hbWUiOm51bGwsImlkcE5hbWUiOiJsZGFwIiwiaWRwVWlkIjoidWlkPW1zZXJ2aWxsYSxvPUVESSxkYz1lZGlyZXBvc2l0b3J5LGRjPW9yZyIsImlzcyI6Imh0dHBzOi8vYXV0aC5lZGlyZXBvc2l0b3J5Lm9yZyIsImhkIjoiZWRpcmVwb3NpdG9yeS5vcmciLCJpYXQiOjE3NzYyMTg5MzIsIm5iZiI6MTc3NjIxODkzMiwiZXhwIjoxNzc2MjQ3NzMyfQ.nCGEnB7FcYdCnSIf3ZgtJHaTMQEplJ8wGSDs5PQnnJIfODC_2DnOSfz1U_aFhGCs9PI1sZXzfOqbyFBzcg5kqg"

    edi_token_response = edi_token_client.refresh_token(auth_token=auth_token, edi_token=edi_token)
    response_printer(edi_token_response)

    token = Token(edi_token_response["edi-token"])
    token.validate(Config.PUBLIC_KEY_PATH, algorithm=Config.JWT_ALGORITHM),

def test_create_token():
    edi_token_client = EdiTokenClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=None,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    edi_token_response = edi_token_client.create_token(profile_edi_identifier=Config.PUBLIC_ID, key=Config.AUTH_KEY)
    response_printer(edi_token_response)

    token = Token(edi_token_response["edi-token"])
    token.validate(Config.PUBLIC_KEY_PATH, algorithm=Config.JWT_ALGORITHM),

def test_key_to_token():
    api_key_client = ApiKeyClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=None,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    api_key_response = api_key_client.key_to_token(key=Config.API_KEY)
    response_printer(api_key_response)

    token = Token(api_key_response["edi-token"])
    token.validate(Config.PUBLIC_KEY_PATH, algorithm=Config.JWT_ALGORITHM),



def response_printer(response):
    for k,v in response.items():
        print(f"{k}: {v}")