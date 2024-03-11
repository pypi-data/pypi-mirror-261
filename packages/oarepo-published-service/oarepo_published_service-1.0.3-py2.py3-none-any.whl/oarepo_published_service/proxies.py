from flask import current_app
from werkzeug.local import LocalProxy


def _ext_proxy(attr):
    return LocalProxy(
        lambda: getattr(current_app.extensions["oarepo-published-service"], attr)
    )


current_service = _ext_proxy("service")
"""Proxy to the instantiated published service."""
