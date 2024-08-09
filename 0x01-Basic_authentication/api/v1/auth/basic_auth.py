#!/usr/bin/env python3
"""doc doc doc """
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Authentification """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ extract base64 """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]
