#!/usr/bin/env python3
""" Manage API Authentification """
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth():
    """ Manage API Authentification """
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ require auth """
        if bool(path and excluded_paths):
            path = path + "/" if path[-1] != "/" else path
            for p in excluded_paths:
                if p.endswith("*") and path.startswith(p[:-1]):
                    return False
                if p == path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header """
        if bool(request and "Authorization" in request.headers.keys()):
            return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """doc doc doc"""
        return None
