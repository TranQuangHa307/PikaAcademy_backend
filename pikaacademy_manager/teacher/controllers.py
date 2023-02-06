from logging import getLogger

from common.constants import RoleTypeEnum
from common.models import Pagination
from common.parameters import pagination_parameter, change_password_parameters
from common.res_base import parse, result_all, paginate_result
from flask import request
from flask_restplus import Namespace, Resource
from libs.sql_action import db
from libs.auth import AuthenticatedResource
from werkzeug.security import check_password_hash
from .dao import TeacherDAO, TeacherUserDAO, TeacherUserCourseDAO
from .models import teacher_fields, Teacher
from .parameters import login_parameters, sign_up_parameters, parameter_teacher_courses
from exceptions import UserNotFoundException, EmailExistxception
from flask_jwt_extended import get_jwt_identity, get_jwt_claims
from flask_jwt_extended import create_access_token
from .service import (change_password, sign_up, active_teacher)
from course.dao import CourseDAO

logger = getLogger(__name__)
api = Namespace("teacher", description='Teachers related operations')

teacher_model = api.model("Teacher", teacher_fields)


@api.route("/login")
class Login(Resource):
  """Login apis"""

  @api.doc()
  @api.expect(login_parameters, validate=True)
  def post(self):
    args = login_parameters.parse_args(request)
    teacher_info = (
      db.session.query(Teacher).filter(Teacher.email == args.email,
                                       Teacher.is_active,
                                       Teacher.deleted_flag.isnot(True)).first()
    )
    if teacher_info is None or (
        teacher_info and not check_password_hash(teacher_info.hash_pwd, args.password)
    ):
      raise UserNotFoundException()
    access_token = create_access_token(
      {"id": teacher_info.id, "role": 'teacher', "user_name": teacher_info.full_name})
    login_response = {
      "access_token": access_token,
      "user_role": 'teacher',
    }
    return login_response


@api.route("/me")
class TeacherMe(AuthenticatedResource):
  """Account me apis"""

  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self):
    """Get account info"""
    _id = get_jwt_identity()
    role = get_jwt_claims()["role"]
    if role == RoleTypeEnum.Teacher.value:
      return parse(TeacherDAO.get_by_id(_id))
    return None


@api.route('/change-password')
class ChangePassword(AuthenticatedResource):
  @api.doc()
  @api.expect(change_password_parameters, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Teacher.value])
  def post(self):
    args = change_password_parameters.parse_args(request)
    res = change_password(args)
    return res, 201


@api.route('/sign-up/check')
class SignUpCheck(Resource):
  @api.doc()
  @api.expect(sign_up_parameters, validate=True)
  def post(self):
    args = sign_up_parameters.parse_args(request)
    teacher_info = TeacherDAO.get_by_email(args.email)
    if teacher_info:
      raise EmailExistxception
    return None, 204


@api.route('/sign-up')
class SignUp(Resource):
  @api.doc()
  @api.expect(teacher_model, validate=True)
  def post(self):
    sign_up(api.payload)
    return None, 201


@api.route('/all')
class TeacherAllController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self):
    return result_all(TeacherDAO.get_all())


@api.route('')
class TeacherListController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(TeacherDAO.get_list(paging))

  @api.doc()
  @api.expect(teacher_model, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def post(self):
    TeacherDAO.add(api.payload)
    return None, 201


@api.route('/<teacher_id>')
@api.response(404, 'Teacher not found.')
class CourseController(Resource):
  @api.doc()
  def get(self, teacher_id):
    return parse(TeacherDAO.get_by_id(teacher_id))

  @api.doc()
  @api.expect(teacher_model, validate=True)
  @api.response(204, 'Teacher successfully updated.')
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def put(self, teacher_id):
    TeacherDAO.update(teacher_id, api.payload)
    return None, 204

  @api.doc()
  @api.response(204, "Teacher successfully deleted.")
  @AuthenticatedResource.roles_required(['admin'])
  def delete(self, teacher_id):
    TeacherDAO.delete(teacher_id)
    return None, 204


@api.route('/<teacher_id>/users')
@api.response(404, 'Teacher not found.')
class TeacherUserController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self, teacher_id):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(TeacherUserDAO.get_users_by_teacher_id(paging, teacher_id))


@api.route('/<teacher_id>/user/<user_id>/course')
@api.response(404, 'Teacher not found.')
class TeacherUserCourseController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self, teacher_id, user_id):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(TeacherUserCourseDAO.get_list_by_teacher_user_id(paging, teacher_id, user_id))


@api.route('/inactive')
class TeacherInactive(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def get(self):
    return result_all(TeacherDAO.get_all_inactive())


@api.route('/<teacher_id>/active')
@api.response(404, 'Teacher not found.')
class TeacherActiveController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def put(self, teacher_id):
    active_teacher(teacher_id)
    return None, 204

@api.route('/<teacher_id>/courses')
class TeacherCoursesController(Resource):
  @api.doc()
  @api.expect(parameter_teacher_courses, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Teacher.value])
  def get(self, teacher_id):
    args = parameter_teacher_courses.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(CourseDAO.get_list(paging))
