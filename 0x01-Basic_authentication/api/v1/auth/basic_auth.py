#!/usr/bin/env python3
"""doc doc doc """
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentification """
    def extract_base64_authorization_header(
                 self, authorization_header: str
    ) -> str:
        """ extract base64 """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Base64 decode """
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str):
            try:
                decode_byte = base64.b64decode(base64_authorization_header)
                decode_str = decode_byte.decode("utf-8")
                return decode_str
            except (base64.binascii.Error, UnicodeDecodeError) as error:
                return None
