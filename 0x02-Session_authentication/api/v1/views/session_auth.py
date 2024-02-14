#!/usr/bin/env python3
""" Session auth routes module """

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_user():
    """ Session Authentication
    """

    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"})

    users = User.search({"email": email})

    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    # create user session
    session_id = auth.create_session(user.id)

    out = jsonify(user.to_json())
    out.set_cookie(os.getenv("SESSION_NAME"), session_id)

    return out
