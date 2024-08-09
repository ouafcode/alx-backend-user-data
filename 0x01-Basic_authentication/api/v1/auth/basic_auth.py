#!/usr/bin/env python3
"""doc doc doc """
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
import base64
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ User Cridentials """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Basic - User object """
        if user_email is None or user_pwd is None:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({"email": user_email})
            if user:
                if user[0].is_valid_password(user_pwd):
                    return user[0]
                else:
                    return None
        except Exception:
            return None
        return None
