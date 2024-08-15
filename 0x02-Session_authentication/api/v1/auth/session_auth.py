#!/usr/bin/env python3
"""doc doc doc """
from typing import List, TypeVar
from uuid import uuid4
from flask import request
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ docs docs """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ docs docs """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        Session_ID = uuid4()
        self.user_id_by_session_id[str(Session_ID)] = user_id
        return str(Session_ID)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ docs docs """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ docs docs """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        docs docs
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
