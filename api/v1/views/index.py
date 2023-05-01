#!/usr/bin/python3
"""
creates routes
"""

from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """returns JSON status"""
    return {"status": "OK"}
