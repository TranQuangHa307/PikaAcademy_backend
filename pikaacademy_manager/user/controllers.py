from logging import getLogger

from common.parameters import pagination_parameter
from common.res_base import parse, paginate_result
from exceptions import UserNotFoundException, EmailExistxception
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_restplus import Namespace, Resource
from libs.auth import AuthenticatedResource
from libs.constants import RoleTypeEnum
from google.oauth2 import id_token
from google.auth.transport import requests
from werkzeug.security import check_password_hash

from .dao import UserDAO, UserLikeCourseDAO, UserPurchaseCourseDAO
from .models import user_fields, user_like_course_fields, user_purchase_course_fields
from .parameters import login_parameters, sign_up_parameters, pagination_parameter_transactions_user, \
  change_password_parameters, login_google_parameters
from .service import (user_like_course, sign_up, change_password, user_purchase_course)

logger = getLogger(__name__)
api = Namespace("user", description="User related operations")
user_model = api.model("User", user_fields)
user_like_course_model = api.model("User like course", user_like_course_fields)
user_purchase_course_model = api.model("User purchase course", user_purchase_course_fields)


@api.route('/login')
class Login(Resource):
  @api.doc()
  @api.expect(login_parameters, validate=True)
  def post(self):
    args = login_parameters.parse_args(request)
    user_info = UserDAO.get_by_email(args.email)
    if not user_info or (user_info and not check_password_hash(user_info.hash_pwd, args.password)):
      raise UserNotFoundException()
    access_token = create_access_token(
      {"id": user_info.id, "role": 'user', "user_name": user_info.email}
    )
    login_response = {
      "access_token": access_token,
      "user_role": 'user'
    }
    return login_response

@api.route('/google_auth')
class LoginByGoogle(Resource):
  @api.doc()
  @api.expect(login_google_parameters, validate=True)
  def post(self):
    args = login_google_parameters.parse_args(request)
    id_info = id_token.verify_oauth2_token(
      args.googleToken.replace("Bearer ", ''),
      requests.Request(),
      "684358347602-9e5kiu1cg8ctram5jpbj620hlo40skfk.apps.googleusercontent.com"
    )
    user_info = UserDAO.get_by_email(id_info["email"])
    if not user_info:
      raise UserNotFoundException()
    access_token = create_access_token(
      {"id": user_info.id, "role": 'user', "user_name": user_info.email}
    )
    login_response = {
      "access_token": access_token,
      "user_role": 'user'
    }
    return login_response


@api.route('/sign-up/check')
class SignUpCheck(Resource):
  @api.doc()
  @api.expect(sign_up_parameters, validate=True)
  def post(self):
    args = sign_up_parameters.parse_args(request)
    user_info = UserDAO.get_by_email(args.email)
    if user_info:
      raise EmailExistxception
    return None, 204


@api.route('/sign-up')
class SignUp(Resource):
  @api.doc()
  @api.expect(user_model, validate=True)
  def post(self):
    sign_up(api.payload)
    return None, 201


@api.route('/change-password')
class ChangePassword(AuthenticatedResource):
  @api.doc()
  @api.expect(change_password_parameters, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value])
  def post(self):
    args = change_password_parameters.parse_args(request)
    res = change_password(args)
    return res, 201


@api.route("/me")
class UserMe(AuthenticatedResource):
  """User me apis"""

  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value])
  def get(self):
    """Get account info"""
    _id = get_jwt_identity()
    return parse(UserDAO.get_by_id(_id))


@api.route('')
class UserListController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def get(self):
    args = pagination_parameter.parse_args(request)
    return paginate_result(UserDAO.get_list(args))

  @api.doc()
  @api.expect(user_model, validate=True)
  @api.response(204, 'User successfully created.')
  def post(self):
    UserDAO.add(api.payload)
    return None, 201


@api.route('/<user_id>')
@api.response(404, 'User not found')
class UserController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.User.value, 'teacher'])
  def get(self, user_id):
    return parse(UserDAO.get_by_id(user_id))

  @api.doc()
  @api.expect(user_model, validate=True)
  @api.response(204, 'User successfully updated.')
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.User.value])
  def put(self, user_id):
    UserDAO.update(user_id, api.payload)
    return None, 204

  @api.doc()
  @api.response(204, "User successfully deleted.")
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def delete(self, user_id):
    UserDAO.delete(user_id)
    return None, 204


@api.route('/user-like-course')
class UserLikeCourseController(AuthenticatedResource):
  @api.doc()
  @api.expect(user_like_course_model, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value])
  def post(self):
    return user_like_course(api.payload), 201


@api.route('/<user_id>/user-like-course')
class ListFavoriteCourseController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value, RoleTypeEnum.Admin.value])
  def get(self, user_id):
    args = pagination_parameter.parse_args(request)
    return paginate_result(UserLikeCourseDAO.get_list(args, user_id))


@api.route('/user-purchase-course')
class UserPurchaseCourseController(AuthenticatedResource):
  @api.doc()
  @api.expect(user_purchase_course_model, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value])
  def post(self):
    user_purchase_course(api.payload)
    return None, 201


@api.route('/<user_id>/user-purchase-course')
class ListPurchasedCourseController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value, RoleTypeEnum.Admin.value])
  def get(self, user_id):
    args = pagination_parameter.parse_args(request)
    return paginate_result(UserPurchaseCourseDAO.get_list(args, user_id))





