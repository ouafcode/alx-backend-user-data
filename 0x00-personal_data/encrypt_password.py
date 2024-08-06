#!/usr/bin/env python3
""" Encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Encrypting passwords """
    password = b"{password}"
    return  bcrypt.hashpw(password, bcrypt.gensalt())
