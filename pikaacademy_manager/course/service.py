from .dao import CourseDAO, PriceDAO, DiscountPromotionDAO
from werkzeug.exceptions import InternalServerError
from logging import getLogger

logger = getLogger(__name__)


def add_courses(body):
  try:
    course_obj = {
      'name': body["name"],
      'description': body["description"],
      'about': body["about"],
      'url_image': body["url_image"],
      'url_intro_video': body["url_intro_video"],
      'result': body["result"],
      'level': body["level"],
      'interests_id': body["interests_id"],
      'category_id': body["category_id"],
      'teacher_id': body["teacher_id"],
      'created_by': body["created_by"],
      'updated_by': body["updated_by"]
    }
    course_id = CourseDAO.add(course_obj)
    if course_id:
      price_obj = {
        'course_id': course_id,
        'price': body["price"],
        'is_active': True
      }
      PriceDAO.add(price_obj)
      if body["discount"]:
        discount_promotion_obj = {
          'course_id': course_id,
          'discount': body["discount"],
          'begin_date': body["begin_date"],
          'end_date': body["end_date"],
          'is_active': True
        }
        DiscountPromotionDAO.add(discount_promotion_obj)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))


def update_course(course_id, body):
  try:
    course_obj = {
      'name': body["name"],
      'description': body["description"],
      'about': body["about"],
      'url_image': body["url_image"],
      'url_intro_video': body["url_intro_video"],
      'result': body["result"],
      'level': body["level"],
      'interests_id': body["interests_id"],
      'category_id': body["category_id"],
      'teacher_id': body["teacher_id"],
      'created_by': body["created_by"],
      'updated_by': body["updated_by"]
    }
    CourseDAO.update(course_id, course_obj)
    price = PriceDAO.get_by_id(body["price_id"])
    if price.price != body["price"]:
      PriceDAO.inactive(body["price_id"])
      price_obj = {
        'course_id': course_id,
        'price': body["price"],
        'is_active': True
      }
      PriceDAO.add(price_obj)
    if body["discount_promotion_id"]:
      discount_promotion = DiscountPromotionDAO.get_by_id(body["discount_promotion_id"])
      if discount_promotion.discount != body["discount"] or discount_promotion.begin_date != body[
        "begin_date"] or discount_promotion.end_date != body["end_date"]:
        logger.info('update')
        DiscountPromotionDAO.inactive(body["discount_promotion_id"])
    if body["discount"]:
      discount_promotion_obj = {
        'course_id': course_id,
        'discount': body["discount"],
        'begin_date': body["begin_date"],
        'end_date': body["end_date"],
        'is_active': True
      }
      DiscountPromotionDAO.add(discount_promotion_obj)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
