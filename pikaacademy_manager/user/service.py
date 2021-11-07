from course.dao import CourseDAO
from cart.dao import CartDAO
from common.mail.send_mail import (sign_up_successfully)
from werkzeug.exceptions import InternalServerError
from logging import getLogger
from .dao import UserLikeCourseDAO, UserDAO

logger = getLogger(__name__)
def user_like_course(params):
  try:
    course = CourseDAO.get_by_id(params["course_id"])
    res = None
    if course:
      user_like_course_db = UserLikeCourseDAO.get_by_id(params["course_id"], params["user_id"])
      if user_like_course_db:
        UserLikeCourseDAO.delete(user_like_course_db.id)
        number_likes = course.likes - 1
      else:
        _id = UserLikeCourseDAO.add(params)
        number_likes = course.likes + 1
        res = _id
      CourseDAO.update(course.id, {"likes": number_likes})
    return res
  except Exception as e:
    raise InternalServerError(str(e.__cause__))

def sign_up(body):
  try:
    user = UserDAO.add(body)
    if user:
      cart = {
        'user_id': user.id
      }
      CartDAO.add(cart)
      sign_up_successfully(body["email"], user)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
