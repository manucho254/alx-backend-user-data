#!/usr/bin/env python3
""" Basic auth module
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """get Base64 part of the Authorization
        header for a Basic Authentication
        """
        start = "Basic "

        if (
            authorization_header is None
            or not isinstance(authorization_header, str)
            or start not in authorization_header
        ):
            return

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Basic - Base64 decode"""

        if base64_authorization_header is None or not isinstance(
            base64_authorization_header, str
        ):
            return
        
        try: 
            return base64.b64decode(base64_authorization_header).decode("utf-8")
        except Exception as e:
            return