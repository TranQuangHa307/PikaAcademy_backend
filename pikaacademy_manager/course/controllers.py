from logging import getLogger

from chapter.dao import ChapterDAO
from chapter.schemas import ChapterSchema
from common.constants import RoleTypeEnum
from common.models import Pagination
from common.parameters import pagination_parameter
from common.res_base import parse, paginate_result
from flask import request
from flask_restplus import Namespace, reqparse, Resource
from libs.auth import AuthenticatedResource
from .dao import CourseDAO
from .models import course_fields
from .service import (add_courses, update_course)

logger = getLogger(__name__)
api = Namespace("course", description='Courses related operations')

course_model = api.model("Course", course_fields)

user_parameter = reqparse.RequestParser()
user_parameter.add_argument("id", type=int, location="args")


@api.route('')
class CourseListController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def get(self):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(CourseDAO.get_list(paging))

  @api.doc()
  @api.expect(course_model, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def post(self):
    add_courses(api.payload)
    return None, 201


@api.route('/<course_id>')
@api.response(404, 'Course not found.')
class CourseController(Resource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def get(self, course_id):
    return parse(CourseDAO.get_by_id(course_id))

  @api.doc()
  @api.expect(course_model, validate=True)
  @api.response(204, 'Course successfully updated.')
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def put(self, course_id):
    update_course(course_id, api.payload)
    return None, 204

  @api.doc()
  @api.response(204, "Course successfully deleted.")
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def delete(self, course_id):
    CourseDAO.delete(course_id)
    return None, 204


@api.route('/<course_id>/chapter')
class CourseChapterController(Resource):
  @api.doc()
  def get(self, course_id):
    chapter = ChapterSchema(many=True)
    return chapter.dump(ChapterDAO.get_by_course_id(course_id))
