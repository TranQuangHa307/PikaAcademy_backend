from logging import getLogger

from common.res_base import parse
from exceptions import UserNotFoundException
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_restplus import Namespace, Resource, reqparse
from libs.auth import AuthenticatedResource
from libs.sql_action import db
from sqlalchemy import or_
from werkzeug.security import check_password_hash

from .dao import AdminAccountDAO
from .models import AdminAccount

logger = getLogger(__name__)

api = Namespace("admin")

login_parameters = reqparse.RequestParser()
login_parameters.add_argument("username", type=str, required=True, location="form", default="", help="User name")
login_parameters.add_argument("password", type=str, required=True, location="form", default="", help="User password")


@api.route("/login")
class Login(Resource):
    """Login apis"""

    @api.doc()
    @api.expect(login_parameters, validate=True)
    def post(self):
        args = login_parameters.parse_args(request)
        admin_info = (
            db.session.query(AdminAccount).filter(
                or_(AdminAccount.user_name == args.username, AdminAccount.email == args.username),
                AdminAccount.deleted_flag.isnot(True)).first()
        )
        if admin_info is None or (
                admin_info and not check_password_hash(admin_info.password, args.password)
        ):
            raise UserNotFoundException()
        access_token = create_access_token(
            {"id": admin_info.id, "role": admin_info.role, "user_name": admin_info.user_name})
        login_response = {
            "access_token": access_token,
            "user_role": admin_info.role,
        }
        return login_response


@api.route("/me")
class AccountMe(AuthenticatedResource):
    """Account me apis"""

    @api.doc()
    def get(self):
        """Get account info"""
        _id = get_jwt_identity()
        return parse(AdminAccountDAO.get_account_by_id(account_id=_id))
