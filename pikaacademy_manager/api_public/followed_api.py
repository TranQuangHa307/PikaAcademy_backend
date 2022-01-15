from logging import getLogger

from common.res_base import parse
from flask_restplus import Namespace, Resource

from followed.dao import FollowerDAO

logger = getLogger(__name__)

api = Namespace('api/followed', description="Public APIs For Followed")


@api.route('/user/<user_id>/teacher/<teacher_id>')
class InterestsListController(Resource):
  @api.doc()
  def get(self, user_id, teacher_id):
    return parse(FollowerDAO.get_by_user_teacher_id(user_id, teacher_id))


@api.route('/teacher/<teacher_id>')
class FollowedTeacherController(Resource):
  @api.doc()
  def get(self, teacher_id):
    return parse(FollowerDAO.get_total_followers(teacher_id))
