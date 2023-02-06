from logging import getLogger

from chapter.dao import ChapterDAO
from chapter.schemas import ChapterSchema
from common.constants import RoleTypeEnum
from common.models import Pagination
from common.parameters import pagination_parameter
from common.res_base import parse, paginate_result, result_all
from flask import request
from flask_restplus import Namespace, reqparse, Resource
from libs.auth import AuthenticatedResource
from user.dao import UserByCourse, UserLikeCourseDAO

from .dao import CourseDAO, CourseTeacherDAO, MaterialDAO
from .models import course_fields
from .service import (add_courses, update_course, release, active)

logger = getLogger(__name__)
api = Namespace("course", description='Courses related operations')

course_model = api.model("Course", course_fields)

user_parameter = reqparse.RequestParser()
user_parameter.add_argument("id", type=int, location="args")


@api.route('')
class CourseListController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(CourseDAO.get_list(paging))

  @api.doc()
  @api.expect(course_model, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def post(self):
    add_courses(api.payload)
    return None, 201


@api.route('/<course_id>')
@api.response(404, 'Course not found.')
class CourseController(Resource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self, course_id):
    return parse(CourseDAO.get_by_id(course_id))

  @api.doc()
  @api.expect(course_model, validate=True)
  @api.response(204, 'Course successfully updated.')
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def put(self, course_id):
    update_course(course_id, api.payload)
    return None, 204

  @api.doc()
  @api.response(204, "Course successfully deleted.")
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def delete(self, course_id):
    CourseDAO.delete(course_id)
    return None, 204


@api.route('/<course_id>/chapter')
class CourseChapterController(Resource):
  @api.doc()
  def get(self, course_id):
    chapter = ChapterSchema(many=True)
    return chapter.dump(ChapterDAO.get_by_course_id(course_id))


@api.route('/<course_id>/users')
class CourseUserController(Resource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  def get(self, course_id):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(UserByCourse.get_list_by_course_id(paging, course_id))


@api.route('/<course_id>/likes')
class CourseLikeController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self, course_id):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(UserLikeCourseDAO.get_list_by_course_id(paging, course_id))


@api.route('/teacher/<teacher_id>/top/<status>')
class CourseTeacherTopController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self, teacher_id, status):
    return result_all(CourseTeacherDAO.get_top_course_by_teacher_id(teacher_id, status))


@api.route('/<course_id>/material')
class CourseMaterialController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
  def get(self, course_id):
    return result_all(MaterialDAO.get_list_by_course_id(course_id))

@api.route('/inactive')
class CourseInactive(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def get(self):
    return result_all(CourseDAO.get_all_inactive())


@api.route('/<course_id>/active')
class CourseActive(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def put(self, course_id):
    active(course_id)
    return None, 204


@api.route('/<course_id>/release')
class CourseRelease(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def put(self, course_id):
    release(course_id)
    return None, 204
