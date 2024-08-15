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
