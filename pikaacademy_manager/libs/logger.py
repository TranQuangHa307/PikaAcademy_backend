# -*- coding: utf-8 -*-
import logging
import sys

from flask import request

from .request_id import RequestIDLogFilter

logger = logging.getLogger(__name__)


def init_logger(logLevel):
    handler = logging.StreamHandler(stream=sys.stdout)
    log_format = "%(request_id)s| %(name)-30s | %(levelname)-7s | %(message)s"
    handler.addFilter(RequestIDLogFilter())
    logging.basicConfig(
        level=logLevel,
        handlers=[handler],
        format=log_format,
        datefmt="%Y-%m-%d %H:%M:%S")


class FlaskLogger(object):

    def __init__(self, app):
        logger.info("Middleware - FlaskLogger Enabled")
        app.before_request(self.before_request)
        app.after_request(self.after_request)

    @staticmethod
    def before_request():
        logger.info(
            "Request - %s %s",
            request.method.upper(), request.path
        )

    @staticmethod
    def after_request(response):
        logger.info(
            "Response - %s %s - Status: %s",
            request.method.upper(), request.path, response.status_code
        )
        return response
