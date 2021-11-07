from .dao import InterestsDAO
from .schemas import InterestsSchema
from logging import getLogger

logger = getLogger(__name__)


def get_interests_by_id(interests_id):
  interests = InterestsDAO.get_interests_by_id(interests_id)
  res = {}
  logger.info(f'{interests}')
  for item in interests:
    if not res:
      res = {
        "id": item.id,
        "name": item.name,
        "description": item.description,
        "url_image": item.url_image,
        "categories": []
      }
    res["categories"].append({
      "id": item.category_id,
      "name": item.category_name,
      "url_image": item.category_url_image
    })
  logger.info(f'{res}')
  interests_schema = InterestsSchema()
  return interests_schema.dump(res)
