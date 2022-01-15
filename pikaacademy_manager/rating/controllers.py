from logging import getLogger

from common.constants import RoleTypeEnum
from common.models import Pagination
from common.parameters import pagination_parameter
from common.res_base import paginate_result, parse
from flask import request
from flask_restplus import Namespace, Resource
from libs.auth import AuthenticatedResource

from .dao import RatingDAO
from .models import rating_fields
from .service import (addRating)

logger = getLogger(__name__)
api = Namespace("rating", description='Rating related operations')

rating_model = api.model("Rating", rating_fields)


@api.route('/course/<course_id>')
class RatingCourseController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
  def get(self, course_id):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(RatingDAO.get_by_course_id(paging, course_id))


@api.route('/user/<user_id>/<teacher_id>')
class RatingUserController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self, user_id, teacher_id):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(RatingDAO.get_list_by_user_id(paging, user_id, teacher_id))


@api.route('/course/<course_id>/rating')
class RatingNumberCourseController(Resource):
  @api.doc()
  def get(self, course_id):
    return parse(RatingDAO.get_rating_course(course_id))


@api.route('')
class RatingListController(AuthenticatedResource):
  @api.doc()
  @api.expect(rating_model, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
  def post(self):
    addRating(api.payload)
    return None, 201
