#!/usr/bin/python3
"""
creates routes
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """returns JSON status"""
    return jsonify({"status": "OK"})
