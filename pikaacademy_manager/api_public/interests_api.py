from logging import getLogger
from common.res_base import result_all, parse
from category.dao import CategoryDAO
from flask_restplus import Namespace, Resource
from interests.dao import InterestsDAO
logger = getLogger(__name__)

api = Namespace('api/interests', description="Public APIs For Interests")

@api.route('')
class InterestsListController(Resource):
  @api.doc()
  def get(self):
    return result_all(InterestsDAO.get_all())

@api.route('/<interests_id>')
@api.response(404, 'Interests not found.')
class InterestsController(Resource):
  @api.doc()
  def get(self, interests_id):
    return parse(InterestsDAO.get_by_id(interests_id))

@api.route('/<interests_id>/categories')
@api.response(404, 'Interests not found.')
class CategoriesListController(Resource):
  @api.doc()
  def get(self, interests_id):
    return result_all(CategoryDAO.get_list_by_interests_id(interests_id))

