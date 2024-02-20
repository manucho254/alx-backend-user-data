#!/usr/bin/env python3
""" Auth module
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """hash user password"""

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(14))


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user

        Args:
            email (str): user email
            password (str): user password
        Returns:
            User: user object
        """

        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {email} already exists")

        new_user = self._db.add_user(email, _hash_password(password))
        self._db._session.add(new_user)
        self._db._session.commit()
