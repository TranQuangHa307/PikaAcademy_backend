"""
Middleware to inject Request-Id header in every Flask request to debug easier.

Using:
    FlaskRequestID(app=your_flask_app)
"""
import logging
from uuid import uuid4

from flask import g, has_app_context


logger = logging.getLogger(__name__)


def current_request_id():  # pragma: no cover
    if has_app_context():
        return getattr(g, 'request_id', None)
    return None


def generate_request_id():
    return str(uuid4().hex)[16:]


class FlaskRequestID(object):
    def __init__(self, app):
        logger.info("Middleware - RequestID Enabled")
        app.before_request(self.before_request)
        app.after_request(self.after_request)

    @staticmethod
    def before_request():
        g.request_id = generate_request_id()

    @staticmethod
    def after_request(response):
        response.headers["Request-Id"] = g.request_id
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'GET, HEAD, POST, OPTIONS, PUT, PATCH, DELETE'
        allow_header = "Keep-Alive, User-Agent, X-Requested-With, If-Modified-Since, Cache-Control, Content-Type, token"
        response.headers['Access-Control-Allow-Headers'] = allow_header
        response.headers['Access-Control-Max-Age'] = '1728000'

        return response


class RequestIDLogFilter(logging.Filter):  # pragma: no cover
    """
    Log filter to inject the current request id of the request under
    `log_record.request_id`
    """

    def filter(self, record):
        if current_request_id():
            record.request_id = "| ReqID: {} ".format(current_request_id())
        else:
            record.request_id = ""
        return record
