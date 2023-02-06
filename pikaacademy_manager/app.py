from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

from api.v1 import api
from libs.logger import init_logger
# from libs.sentry import init_sentry_flask
from flask_cors import CORS

def create_app():
    init_logger('DEBUG')
    my_app = Flask(__name__)
    my_app.config.from_pyfile('config.py')
    db = SQLAlchemy()
    db.init_app(my_app)
    ma = Marshmallow()
    ma.init_app(my_app)
    CORS(my_app, resources=r"/*", origins=["http://localhost:8080"])
    my_app.wsgi_app = ProxyFix(my_app.wsgi_app)
    api.init_app(my_app)
    jwt_manager = JWTManager()
    jwt_manager.init_app(my_app)
    jwt_manager._set_error_handler_callbacks(api)

    @jwt_manager.user_claims_loader
    def add_claims_to_access_token(user):
        return {
            'role': user["role"],
            'user_name': user["user_name"]
        }

    @jwt_manager.user_identity_loader
    def user_identity_lookup(user):
        return user["id"]

    return my_app


app = create_app()
