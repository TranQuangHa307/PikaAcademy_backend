# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration
# from logging import getLogger
# from config import SENTRY_DNS, CURRENT_ENV, RELEASE_VERSION
#
# logger = getLogger(__name__)
#
#
# def init_sentry_flask():
#     """Initial sentry flask"""
#     logger.info(f"BEGIN | Initial sentry for env: {CURRENT_ENV} release: {RELEASE_VERSION}")
#     sentry_sdk.init(
#         dsn=SENTRY_DNS,
#         environment=CURRENT_ENV,
#         integrations=[FlaskIntegration()],
#         release=RELEASE_VERSION
#     )
#     logger.info(f"FINISH | Initial sentry for env: {CURRENT_ENV} release: {RELEASE_VERSION}")
