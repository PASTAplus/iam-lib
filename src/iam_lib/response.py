#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    response

:Synopsis:
    Generic HTTP response object to provide abstraction between the requests package
    and IAM.

:Author:
    servilla

:Created:
    5/11/25
"""
import requests

class Response:
    def __init__(self, response: requests.Response):
        self._status_code = response.status_code
        self._reason = response.reason
        self._headers = dict(response.headers)
        self._cookies = dict(response.cookies)
        self._body = response.text

    @property
    def status_code(self):
        return self._status_code

    @property
    def reason(self):
        return self._reason

    @property
    def headers(self):
        return self._headers

    @property
    def cookies(self):
        return self._cookies

    @property
    def body(self):
        return self._body