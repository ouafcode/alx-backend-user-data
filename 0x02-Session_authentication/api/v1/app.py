#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
if os.getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()
elif os.getenv("AUTH_TYPE") == "auth":
    auth = Auth()
elif os.getenv("AUTH_TYPE") == "session_auth":
    auth = SessionAuth()


@app.before_request
def validation():
    """before_request handler"""
    if auth:
        excluded_paths = [
            "/api/v1/status/",
            "/api/v1/unauthorized/",
            "/api/v1/forbidden/",
            "/api/v1/auth_session/login/",
        ]
        if auth.require_auth(request.path, excluded_paths):
            cookie = auth.session_cookie(request)
            if auth.authorization_header(request) is None and cookie is None:
                abort(401)
            if not auth.current_user(request):
                abort(403)

        request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorised(error) -> str:
    """ Unauthorised
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "127.0.0.1")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
