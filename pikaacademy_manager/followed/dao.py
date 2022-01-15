from common.models import Pagination
from libs.sql_action import db
from sqlalchemy import desc
from sqlalchemy import func
from user.models import User
from werkzeug.exceptions import InternalServerError

from .models import Followed


class FollowerDAO(object):

  @staticmethod
  def get_follower_by_teacher_id(args: Pagination, teacher_id):
    try:
      res_query = db.session.query(
        User.id,
        User.first_name,
        User.last_name,
        User.url_avatar,
        User.email,
        User.phone_number,
        User.date_of_birth,
        Followed.id,
        Followed.updated_at.label('followed_time')
      ) \
        .join(Followed, Followed.user_id == User.id) \
        .filter(Followed.teacher_id == teacher_id,
                Followed.is_active,
                Followed.deleted_flag.isnot(True),
                User.deleted_flag.isnot(True))
      res_query = res_query.group_by(User.id, Followed.id).order_by(desc(Followed.updated_at)).paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_all_follower_by_teacher_id(teacher_id):
    try:
      res_query = db.session.query(
        User.id,
        User.first_name,
        User.last_name,
        User.url_avatar,
        User.email,
        User.phone_number,
        User.date_of_birth,
        Followed.id,
        Followed.updated_at.label('followed_time')
      ) \
        .join(Followed, Followed.user_id == User.id) \
        .filter(Followed.teacher_id == teacher_id,
                Followed.is_active,
                Followed.deleted_flag.isnot(True),
                User.deleted_flag.isnot(True))
      res_query = res_query.group_by(User.id, Followed.id).order_by(desc(Followed.updated_at)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_total_followers(teacher_id):
    try:
      res_query = db.session.query(
        Followed.teacher_id.label('teacher_id'),
        func.count(Followed.user_id).label('total')). \
        filter(Followed.teacher_id == teacher_id,
               Followed.is_active,
               Followed.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_user_teacher_id(user_id, teacher_id):
    try:
      res_query = db.session.query(
        Followed.id.label("id"),
        Followed.user_id.label("user_id"),
        Followed.teacher_id.label("teacher_id"),
        Followed.is_active.label("is_active")
      ).filter(Followed.user_id == user_id,
               Followed.teacher_id == teacher_id,
               Followed.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      followed = Followed(params)
      Followed.create(followed)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update(followed_id, data_dict):
    try:
      Followed.update(followed_id, data_dict)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
