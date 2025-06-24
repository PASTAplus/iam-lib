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


def response_printer(response):
    for k,v in response.items():
        print(f"{k}: {v}")