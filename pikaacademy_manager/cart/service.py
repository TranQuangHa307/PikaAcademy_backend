from .dao import CartCourseDAO
from werkzeug.exceptions import InternalServerError


def add_cart_course(params):
  try:
    cart_course = CartCourseDAO.get_by_course_and_cart(params['course_id'], params['cart_id'])
    if not cart_course:
      CartCourseDAO.add(params)
  except Exception as e:
    raise InternalServerError(e.__cause__)
