from logging import getLogger

from cart.dao import CartDAO
from common.mail.send_mail import (sign_up_successfully)
from course.dao import CourseDAO
from teacher.dao import TeacherDAO
from werkzeug.exceptions import InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from .dao import UserLikeCourseDAO, UserDAO

logger = getLogger(__name__)


def user_like_course(params):
  try:
    course = CourseDAO.get_by_id(params["course_id"])
    teacher = TeacherDAO.get_by_id(course.teacher_id)
    res = None
    if course:
      user_like_course_db = UserLikeCourseDAO.get_by_id(params["course_id"], params["user_id"])
      if user_like_course_db:
        UserLikeCourseDAO.delete(user_like_course_db.id)
        number_likes = course.likes - 1
        number_likes_teacher = teacher.likes - 1
      else:
        _id = UserLikeCourseDAO.add(params)
        number_likes = course.likes + 1
        number_likes_teacher = teacher.likes + 1
        res = _id
      CourseDAO.update(course.id, {"likes": number_likes})
      TeacherDAO.update(teacher.id, {"likes": number_likes_teacher})
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


def change_password(body):
  try:
    logger.info(f'body: {body}')
    user = UserDAO.get_by_id(body["id"])
    res = {
      "message": '',
      "status": False
    }
    if user:
      logger.info(f'user: {user}')
      user_info = UserDAO.get_by_email(user.email)
      if not check_password_hash(user_info.hash_pwd, body["current_pw"]):
        res["message"] = 'Incorrect password'
      else:
        if body["new_pw"] != body["confirm_pw"]:
          res["message"] = 'Your password and confirmation password do not match.'
        else:
          UserDAO.update(body["id"], {"hash_pwd": generate_password_hash(body["new_pw"])})
          res["message"] = "Change password successfully"
          res["status"] = True
    else:
      res["message"] = 'User not found'
    return res
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
