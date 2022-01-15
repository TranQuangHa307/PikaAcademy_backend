from common.models import Pagination
from course.models import Course
from libs.sql_action import db
from sqlalchemy import desc
from sqlalchemy import func
from user.models import User
from werkzeug.exceptions import InternalServerError

from .models import Rating


class RatingDAO(object):
  @staticmethod
  def get_by_course_id(args: Pagination, course_id):
    try:
      res_query = db.session.query(
        Rating.id,
        Rating.rating,
        Rating.comment,
        Rating.course_id,
        Rating.user_id,
        Rating.created_at,
        User.url_avatar.label('user_url_avatar'),
        User.first_name.label('user_first_name'),
        User.last_name.label('user_last_name')
      ).join(User, User.id == Rating.user_id) \
        .filter(Rating.course_id == course_id,
                Rating.deleted_flag.isnot(True),
                User.deleted_flag.isnot(True))
      res_query = res_query.order_by(desc(Rating.created_at)) \
        .paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_list_by_user_id(args: Pagination, user_id, teacher_id):
    try:
      res_query = db.session.query(
        Rating.id,
        Rating.rating,
        Rating.comment,
        Rating.course_id,
        Rating.user_id,
        Rating.created_at,
        Course.name.label('course_name'),
        Course.url_image.label('course_url_image')
      ).join(Course, Course.id == Rating.course_id).filter(Rating.user_id == user_id,
                                                           Course.teacher_id == teacher_id,
                                                           Rating.deleted_flag.isnot(True),
                                                           Course.deleted_flag.isnot(True))
      res_query = res_query.order_by(desc(Rating.created_at)).paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_rating_course(course_id):
    try:
      res_query = db.session.query(
        Course.id,
        (func.sum(Rating.rating) / func.count(Rating.id)).label("rating")
      ).join(Rating, Rating.course_id == Course.id) \
        .filter(Course.id == course_id,
                Course.deleted_flag.isnot(True),
                Rating.deleted_flag.isnot(True)).group_by(Course.id).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_rating_teacher(teacher_id):
    try:
      res_query = db.session.query(
        Course.teacher_id,
        (func.sum(Rating.rating) / func.count(Rating.id)).label("rating")
      ).join(Rating, Rating.course_id == Course.id) \
        .filter(Course.teacher_id == teacher_id,
                Course.deleted_flag.isnot(True),
                Rating.deleted_flag.isnot(True)).group_by(Course.teacher_id).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      rating = Rating(params)
      Rating.create(rating)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
