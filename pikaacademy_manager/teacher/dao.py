from libs.sql_action import db, safe_commit
from sqlalchemy import desc, asc, func, and_
from .models import Teacher
from course.models import Course
from common.models import Pagination
from werkzeug.exceptions import InternalServerError


class TeacherDAO(object):

  @staticmethod
  def get_all():
    try:
      res_query = db.session.query(
        Teacher.id,
        Teacher.full_name,
        Teacher.email,
        Teacher.url_avatar,
        Teacher.date_of_birth,
        Teacher.gender,
        Teacher.phone_number,
        Teacher.about
      ).filter(Teacher.deleted_flag.isnot(True))
      res_query = res_query.group_by(Teacher.id) \
        .order_by(desc(Teacher.created_at)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_list(args: Pagination):
    try:
      res_query = db.session.query(
        Teacher.id,
        Teacher.full_name,
        Teacher.email,
        Teacher.url_avatar,
        Teacher.date_of_birth,
        Teacher.gender,
        Teacher.phone_number,
        Teacher.about
      ).filter(Teacher.deleted_flag.isnot(True))
      if args.keyword:
        res_query = res_query.filter(Teacher.full_name.ilikes(f'%%'))
      res_query = res_query.group_by(Teacher.id) \
        .order_by(desc(Teacher.created_at)) \
        .paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        Teacher.id,
        Teacher.full_name,
        Teacher.email,
        Teacher.url_avatar,
        Teacher.date_of_birth,
        Teacher.gender,
        Teacher.phone_number,
        Teacher.about,
        func.count(Course.id).label('number_course')
      ).outerjoin(Course, and_(Course.teacher_id==Teacher.id,
                          Course.deleted_flag.isnot(True)))\
        .filter(Teacher.id == _id, Teacher.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


  @staticmethod
  def add(params):
    try:
      teacher = Teacher(params)
      Teacher.create(teacher)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


  @staticmethod
  def update(teacher_id, data_dict):
    try:
      Teacher.update(teacher_id, data_dict)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


  @staticmethod
  def delete(teacher_id):
    try:
      Teacher.update(teacher_id, {"deleted_flag": True})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
