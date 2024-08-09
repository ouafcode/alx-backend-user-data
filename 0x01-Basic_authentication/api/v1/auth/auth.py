#!/usr/bin/env python3
""" Manage API Authentification """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Manage API Authentification """
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ require auth """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """doc doc doc"""
        return None
