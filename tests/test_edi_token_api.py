#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    test_edi_token_api

:Synopsis:
    Pytest for the EDI Token API

:Author:
    servilla

:Created:
    6/1/25
"""
from unittest.mock import MagicMock

import daiquiri
import requests


logger = daiquiri.getLogger(__name__)


def test_create_token(edi_token_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"CREATE_TOKEN\": \"OK\"}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    edi_token_client.create_token(
        profile_edi_identifier="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
        key="key"
    )
    assert edi_token_client.response.status_code == 200
    assert edi_token_client.response.text == "{\"CREATE_TOKEN\": \"OK\"}"


def test_revoke_token(edi_token_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"REVOKE_TOKEN\": \"OK\"}"
    )
    mocker.patch.object(requests, "put", return_value=mock_requests_response)
    edi_token_client.revoke_token(
        profile_edi_identifier="EDI-3fa734a7cd6e40998a5c2b5486b6eced",
    )
    assert edi_token_client.response.status_code == 200
    assert edi_token_client.response.text == "{\"REVOKE_TOKEN\": \"OK\"}"


def test_lock_token(edi_token_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"LOCK_TOKEN\": \"OK\"}"
    )
    mocker.patch.object(requests, "delete", return_value=mock_requests_response)
    edi_token_client.lock_token(
        profile_edi_identifier="EDI-3fa734a7cd6e40998a5c2b5486b6eced"
    )
    assert edi_token_client.response.status_code == 200
    assert edi_token_client.response.text == "{\"LOCK_TOKEN\": \"OK\"}"

def test_refresh_token(edi_token_client, cookies, headers, mocker):
    mock_requests_response = MagicMock(
        status_code=200,
        reason="OK",
        headers=headers,
        cookies=cookies,
        text="{\"REFRESH_TOKEN\": \"OK\"}"
    )
    mocker.patch.object(requests, "post", return_value=mock_requests_response)
    auth_token = "dWlkPW1zZXJ2aWxsYSxvPUVESSxkYz1lZGlyZXBvc2l0b3J5LGRjPW9yZypodHRwczovL3Bhc3RhLmVkaXJlcG9zaXRvcnkub3JnL2F1dGhlbnRpY2F0aW9uKjE3NTcyMjYyOTAzNTMqdmV0dGVkKmF1dGhlbnRpY2F0ZWQ=-UHxUknXcB2Ieo38btpXVZ5il0pyoKqMB/RhOBWZ2GNgIHToWRmhqVHjHtWeEyfH25bjHxYJpAFgeaKlJRDQk0vkayvL+XLvsenajfQZTjelVFCgrXyb/tYeagd42P6wUTzhLcvbphns6c316A3J9UI88scN45rjaeBpcj2+FfO0DRp3RQnhgNLzJB9UPT3Ay2QW2h8jwwH4Ls05NDnift7zJ1WOiCC09Va3s0S8sD5JoCyaqOSIlH9b4ZXewO9B0Q0Iq4nDnI3QiBgV6kcCSj6HRg4h5Z0wunZfgVrAiJSWVojkANO4V0+gHDRs1W1BA3ZnGAulH/9OfUb7iad0OGQ=="
    edi_token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJFREktMmY4YTIyODc4ZDMzN2UwOWRkYWJhMTVlZTBlZWU5YmIyOTMzZmQ1NCIsImNuIjoibXNlcnZpbGxhIiwiZW1haWwiOm51bGwsInByaW5jaXBhbHMiOlsiRURJLTA3OGU2ZTNjZWU0ZjdmMjgxMmYxNTA3MDFkYTkzNTFhY2I1MWUwODkiLCJFREktN2JlMzUxMGQwOGRlZjBkZmM2Njc4MjRlYmQ0ZjRmMWJiZDc3MDIzNCIsIkVESS1iZGFlNzQ5NzJlZDcxMGM1NmIxZTBkZjE4Y2NiNmUyM2MzMWY2MGY2Il0sImlzRW1haWxFbmFibGVkIjpmYWxzZSwiaXNFbWFpbFZlcmlmaWVkIjpmYWxzZSwiaWRlbnRpdHlJZCI6MywiaWRwTmFtZSI6ImxkYXAiLCJpZHBVaWQiOiJ1aWQ9bXNlcnZpbGxhLG89RURJLGRjPWVkaXJlcG9zaXRvcnksZGM9b3JnIiwiaWRwQ25hbWUiOiJtc2VydmlsbGEiLCJpc3MiOiJodHRwczovL2F1dGguZWRpcmVwb3NpdG9yeS5vcmciLCJoZCI6ImVkaXJlcG9zaXRvcnkub3JnIiwiaWF0IjoxNzU3MTk3NDkwLCJuYmYiOjE3NTcxOTc0OTAsImV4cCI6MTc1NzIyNjI5MH0.LlD_es5kAMckwCYWLx_AwUEr0Eks33RWtYliy7DmHxiSrkKG1Dfy6-FSIu0Iuj_3BarP0LoP04BWR0h8ACjguw"
    edi_token_client.refresh_token(auth_token=auth_token, edi_token=edi_token)
