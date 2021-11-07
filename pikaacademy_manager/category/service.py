from logging import getLogger

from werkzeug.exceptions import InternalServerError

from .dao import CategoryDAO, InterestsCategoryDao

logger = getLogger(__name__)


def add_category(params):
  try:
    category_id = CategoryDAO.add(params)
    if category_id and params["interests_id"]:
      InterestsCategoryDao.bulk_add(category_id, params["interests_id"])
  except Exception as e:
    raise InternalServerError(str(e.__cause__))


def update_category(category_id, params):
  try:
    category = {
      "name": params["name"],
      "url_image": params["url_image"],
      "created_by": params["created_by"],
      "updated_by": params["updated_by"]
    }
    CategoryDAO.update(category_id, category)
    InterestsCategoryDao.delete_by_category_id(category_id)
    if params["interests_id"]:
      InterestsCategoryDao.bulk_add(category_id, params["interests_id"])
  except Exception as e:
    raise InternalServerError(str(e.__cause__))

def delete_category(category_id):
  try:
    CategoryDAO.delete(category_id)
    InterestsCategoryDao.delete_by_category_id(category_id)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
