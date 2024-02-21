#!/usr/bin/env python3
""" Simple app """

from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def home():
    """home page"""

    return jsonify({"message": "Bienvenue"})


@app.route("/users", method=["POST"], strict_slashes=False)
def register() -> str:
    """register new user"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        message = {"email": email, "message": "user created"}
        return jsonify(message), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
