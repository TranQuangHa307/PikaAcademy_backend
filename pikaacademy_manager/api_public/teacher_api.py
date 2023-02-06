from logging import getLogger

from common.models import Pagination
from common.res_base import paginate_result, parse
from common.parameters import (pagination_parameter)
from flask import request
from flask_restplus import Namespace, Resource
from teacher.dao import TeacherDAO
from user.dao import UserPurchaseCourseDAO
from rating.dao import RatingDAO

logger = getLogger(__name__)

api = Namespace('api/teacher', description='Public APIs For Teacher')


@api.route('')
class TeacherListController(Resource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  def get(self):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(TeacherDAO.get_list(paging, True))


@api.route('/<teacher_id>')
@api.response(404, 'Teacher not found.')
class TeacherController(Resource):
  @api.doc()
  def get(self, teacher_id):
    return parse(TeacherDAO.get_by_id(teacher_id))


@api.route('/<teacher_id>/user/total')
class TeacherUserTotalController(Resource):
  @api.doc()
  def get(self, teacher_id):
    return parse(UserPurchaseCourseDAO.get_user_total_by_teacher_id(teacher_id))

@api.route('/<teacher_id>/rating')
class TeacherRatingController(Resource):
  @api.doc()
  def get(self, teacher_id):
    return parse(RatingDAO.get_rating_teacher(teacher_id))
