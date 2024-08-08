#!/usr/bin/env python3
""" Manage API Authentification """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Manage API Authentification """
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ require auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization_header """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return request
