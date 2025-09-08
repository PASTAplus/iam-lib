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
    client_token = make_token("EDI-6d92693416fde9af9c43fd7cd92d1028eadafa46")
    edi_token_client = EdiTokenClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=client_token,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    auth_token = "dWlkPW1zZXJ2aWxsYSxvPUVESSxkYz1lZGlyZXBvc2l0b3J5LGRjPW9yZypodHRwczovL3Bhc3RhLmVkaXJlcG9zaXRvcnkub3JnL2F1dGhlbnRpY2F0aW9uKjE3NTczMDkwMjA2MjYqdmV0dGVkKmF1dGhlbnRpY2F0ZWQ=-Ayq8K6hSyiz0Mei2GyZqXjMiYqw0EQt7eqdxHb//46oTWRtA3CjUZ5ysiDJQAmMyv4feewaLWMSExBbTqKJyC7wnm9GBVuOqiYi7kjUoFTHlCLozrNgERl5RRJM5nV7+iJ4cgDsqcG4MQbHlxcFEuu+iWeP8nOfEhB4Ee7WSzvCRT5HYbn4lJWgeOgk+A7lfOxtlAv6cKXYsf1q9BDnKz8C0haDiPw+kXzu7FfDPAoAj9CaApCSk1EIxQLVAE7T6UWb/yYnANaGiF/VFRI7/qcJx6i9G4msQLkgHbihgeFr/xOz4znI4QMN31ys8LZP9/TFMoPFkyyNIIMMIyw5thA=="
    edi_token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJFREktMmY4YTIyODc4ZDMzN2UwOWRkYWJhMTVlZTBlZWU5YmIyOTMzZmQ1NCIsImNuIjoibXNlcnZpbGxhIiwiZW1haWwiOm51bGwsInByaW5jaXBhbHMiOlsiRURJLTA3OGU2ZTNjZWU0ZjdmMjgxMmYxNTA3MDFkYTkzNTFhY2I1MWUwODkiLCJFREktN2JlMzUxMGQwOGRlZjBkZmM2Njc4MjRlYmQ0ZjRmMWJiZDc3MDIzNCIsIkVESS1iZGFlNzQ5NzJlZDcxMGM1NmIxZTBkZjE4Y2NiNmUyM2MzMWY2MGY2Il0sImlzRW1haWxFbmFibGVkIjpmYWxzZSwiaXNFbWFpbFZlcmlmaWVkIjpmYWxzZSwiaWRlbnRpdHlJZCI6MywiaWRwTmFtZSI6ImxkYXAiLCJpZHBVaWQiOiJ1aWQ9bXNlcnZpbGxhLG89RURJLGRjPWVkaXJlcG9zaXRvcnksZGM9b3JnIiwiaWRwQ25hbWUiOiJtc2VydmlsbGEiLCJpc3MiOiJodHRwczovL2F1dGguZWRpcmVwb3NpdG9yeS5vcmciLCJoZCI6ImVkaXJlcG9zaXRvcnkub3JnIiwiaWF0IjoxNzU3Mjk2Njg1LCJuYmYiOjE3NTcyOTY2ODUsImV4cCI6MTc1NzMyNTQ4NX0.QI1IQrBr1PajfRuz8_iMUTB1qNcqeVBRUU_M2hR_rBVqznD2oVUSd97IbVposuFXM967VPfB9J6XG22HO6rDNQ"

    edi_token_response = edi_token_client.refresh_token(auth_token=auth_token, edi_token=edi_token)
    response_printer(edi_token_response)

    token = Token(edi_token_response["edi-token"])
    token.validate(Config.PUBLIC_KEY_PATH, algorithm=Config.JWT_ALGORITHM),

def response_printer(response):
    for k,v in response.items():
        print(f"{k}: {v}")