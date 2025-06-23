from iam_lib.api.profile import ProfileClient
from iam_lib.api.resource import ResourceClient
from iam_lib.api.rule import RuleClient
from iam_lib.models.permission import Permission
from tests.config import Config
from tests.utilities import make_token


def test_create_profile():
    token = make_token("EDI-376d4d3e43554771a1dd0a0c52050508")
    profile_client = ProfileClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=token,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    idp_uid = "mathew.sobel@gmail.com"
    profile_response = profile_client.create_profile(idp_uid=idp_uid)
    print(f"*** {idp_uid} ***")
    response_printer(profile_response)
    edi_id = profile_response["edi_id"]
    assert edi_id == "EDI-221c782cc3c84fcba888fadd7cbe708a"


def test_create_resource():
    token = make_token("EDI-221c782cc3c84fcba888fadd7cbe708a")
    resource_client = ResourceClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=token,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    # resource_client.create_resource(
    #     resource_key="http://localhost:8088/package/eml/edi/1790/1",
    #     resource_label="edi.1790.1",
    #     resource_type="package",
    #     parent_resource_key = None
    # )

    resource_client.create_resource(
        resource_key="http://localhost:8088/package/metadata/eml/edi/1790/1",
        resource_label="edi.1790.1",
        resource_type="metadata",
        parent_resource_key = None
    )


def test_create_rule():
    token = make_token("EDI-221c782cc3c84fcba888fadd7cbe708a")
    rule_client = RuleClient(
        scheme=Config.SCHEME,
        host=Config.AUTH_HOST,
        accept=Config.ACCEPT,
        public_key_path=Config.PUBLIC_KEY_PATH,
        algorithm=Config.JWT_ALGORITHM,
        token=token,
        truststore="/etc/ssl/certs/ca-certificates.crt",
    )

    rule_client.create_rule(
        resource_key="http://localhost:8088/package/eml/edi/1790/1",
        principal="EDI-221c782cc3c84fcba888fadd7cbe708a",
        permission=Permission.CHANGEPERMISSION,
    )


def response_printer(response):
    for k,v in response.items():
        print(f"{k}: {v}")