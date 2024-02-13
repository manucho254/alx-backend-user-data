#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Eequire auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header """
        return

    def current_user(self, request=None) -> TypeVar('User'):
        """ get current user """
        return
