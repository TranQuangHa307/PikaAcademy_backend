from common.models import Pagination
from common.res_base import paginate_result, result_all
from libs.sql_action import db, safe_commit
from course.models import Course
from sqlalchemy import desc, and_, func
from werkzeug.exceptions import InternalServerError
from category.models import Category
from .models import Interests
from logging import getLogger

logger = getLogger(__name__)


class InterestsDAO(object):
  @staticmethod
  def get_all():
    try:
      res_query = db.session.query(
        Interests.id,
        Interests.name,
        Interests.description,
        Interests.url_image,
        func.count(Course.id).label("number_course")
      ).outerjoin(Course, and_(Course.interests_id == Interests.id,
                          Course.deleted_flag.isnot(True))) \
        .filter(Interests.deleted_flag.isnot(True)) \
        .group_by(Interests.id) \
        .order_by(desc(Interests.created_at)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_list(args: Pagination):
    try:
      res_query = db.session.query(
        Interests.id,
        Interests.name,
        Interests.description,
        Interests.url_image
      ).filter(Interests.deleted_flag.isnot(True))
      if args.keyword:
        res_query = res_query.filter(Interests.name.ilike(f'%{args.keyword}%'))
      res_query = res_query.group_by(Interests.id) \
        .order_by(desc(Interests.created_at)) \
        .paginate(args.page, args.limit)
      return paginate_result(res_query)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        Interests.id,
        Interests.name,
        Interests.description,
        Interests.url_image
      ).filter(Interests.id == _id, Interests.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def create(params):
    try:
      interests = Interests(params)
      Interests.create(interests)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update(id, data_dict):
    try:
      Interests.update(id, data_dict)
    except Exception:
      raise InternalServerError()

  @staticmethod
  def delete(id):
    try:
      Interests.update(id, {"deleted_flag": True})
    except Exception:
      raise InternalServerError()
