from common.models import Pagination
from common.res_base import paginate_result, result_all
from libs.sql_action import db, safe_commit
from sqlalchemy import desc, and_, func
from werkzeug.exceptions import InternalServerError
from course.models import Course
from .models import Category
from interests.models import Interests

class CategoryDAO(object):
  @staticmethod
  def get_all():
    try:
      res_query = db.session.query(
        Category.id,
        Category.name,
        Category.url_image,
        Category.interests_id
      ).filter(Category.deleted_flag.isnot(True))\
        .order_by(desc(Category.created_at)).all()
      return result_all(res_query)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        Category.id,
        Category.name,
        Category.url_image,
        Category.interests_id
      ).filter(Category.id==_id,Category.deleted_flag.isnot(True))\
        .group_by(Category.id).order_by(desc(Category.created_at)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


  @staticmethod
  def get_list(args: Pagination):
    try:
      res_query = db.session.query(
        Category.id,
        Category.name,
        Category.url_image,
        Category.interests_id,
        Interests.name.label('interests_name')
      ).join(Interests, Interests.id == Category.interests_id).filter(Category.deleted_flag.isnot(True))
      if args.keyword:
        res_query = res_query.filter(Category.name.ilike(f'%{args.keyword}%'))
      res_query = res_query.group_by(Category.id) \
        .order_by(desc(Category.created_at)) \
        .paginate(args.page, args.limit)
      return paginate_result(res_query)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_list_by_interests_id(interests_id):
    try:
      res_query = db.session.query(
        Category.id,
        Category.name,
        Category.url_image,
        Category.interests_id,
        func.count(Course.id).label("course")
      ).outerjoin(Course, and_(Course.category_id == Category.id,
                               Course.deleted_flag.isnot(True)))\
        .filter(Category.interests_id == interests_id,
               Category.deleted_flag.isnot(True))\
        .group_by(Category.id)\
        .order_by(desc(Category.created_at)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      category = Category(params)
      Category.create(category)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update(id, data_dict):
    try:
      Category.update(id, data_dict)
    except Exception:
      raise InternalServerError()

  @staticmethod
  def delete(id):
    try:
      Category.update(id, {"deleted_flag": True})
    except Exception:
      raise InternalServerError()
