from logging import getLogger

from category.dao import CategoryDAO
from common.res_base import parse
from flask_restplus import Namespace, Resource

logger = getLogger(__name__)

api = Namespace('api/category', description="Public APIs for Category")


@api.route('/<category_id>')
@api.response(404, 'Category not found.')
class CategoryController(Resource):
  @api.doc()
  def get(self, category_id):
    return parse(CategoryDAO.get_by_id(category_id))


