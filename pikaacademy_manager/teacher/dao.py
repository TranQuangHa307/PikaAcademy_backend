from common.models import Pagination
from course.models import Course
from libs.sql_action import db
from sqlalchemy import desc, func, and_, or_
from user.models import User, UserPurchaseCourse
from werkzeug.exceptions import InternalServerError
from werkzeug.security import generate_password_hash
from .models import Teacher


class TeacherDAO(object):

  @staticmethod
  def get_by_email(email):
    try:
      res_query = db.session.query(
        Teacher.id,
        Teacher.hash_pwd
      ).filter(Teacher.deleted_flag.isnot(True),
               Teacher.email == email).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

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
  def get_all_inactive():
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
      ).filter(Teacher.deleted_flag.isnot(True), Teacher.is_active.isnot(True))
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
        Teacher.about,
        Teacher.is_active
      ).filter(Teacher.deleted_flag.isnot(True))
      if args.keyword:
        res_query = res_query.filter(Teacher.full_name.ilikes(f'%%'))
      res_query = res_query.group_by(Teacher.id) \
        .order_by(desc(Teacher.followed)) \
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
        Teacher.followed,
        Teacher.likes,
        Teacher.is_active,
        func.count(Course.id).label('number_course')
      ).outerjoin(Course, and_(Course.teacher_id == Teacher.id,
                               Course.deleted_flag.isnot(True))) \
        .filter(Teacher.id == _id, Teacher.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_email(email):
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
        Teacher.followed,
        Teacher.likes
      ).filter(Teacher.email == email, Teacher.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      teacher = Teacher(params)
      if not teacher.hash_pwd:
        teacher.hash_pwd = 'Aa123456@'
      teacher.hash_pwd = generate_password_hash(teacher.hash_pwd)
      Teacher.create(teacher)
      return teacher
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


class TeacherUserDAO(object):
  @staticmethod
  def get_users_by_teacher_id(args: Pagination, teacher_id):
    try:
      res_query = db.session.query(
        User.id,
        User.first_name,
        User.last_name,
        User.url_avatar,
        User.date_of_birth,
        User.email,
        User.phone_number,
        func.count(Course.id).label('count')
      ).join(UserPurchaseCourse, UserPurchaseCourse.user_id == User.id) \
        .join(Course, Course.id == UserPurchaseCourse.course_id) \
        .filter(Course.teacher_id == teacher_id,
                Course.deleted_flag.isnot(True),
                UserPurchaseCourse.deleted_flag.isnot(True),
                User.deleted_flag.isnot(True))
      if args.keyword:
        res_query = res_query.filter(or_(User.first_name.ilikes(f'%{args.keyword}%'),
                                         User.last_name.ilikes(f'%{args.keyword}%')))
      res_query = res_query.group_by(User.id) \
        .order_by(desc(User.created_at)) \
        .paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


class TeacherUserCourseDAO(object):
  @staticmethod
  def get_list_by_teacher_user_id(args: Pagination, teacher_id, user_id):
    try:
      res_query = db.session.query(
        Course.id,
        Course.name,
        Course.description,
        Course.about,
        Course.url_image,
        Course.url_intro_video,
        Course.result,
        Course.views,
        Course.likes,
        Course.purchases,
        Course.level,
        Course.created_at,
        Course.updated_at
      ).join(UserPurchaseCourse, UserPurchaseCourse.course_id == Course.id) \
        .filter(UserPurchaseCourse.user_id == user_id,
                Course.teacher_id == teacher_id,
                Course.deleted_flag.isnot(True),
                UserPurchaseCourse.deleted_flag.isnot(True),
                Course.deleted_flag.isnot(True))
      res_query = res_query.group_by(Course.id) \
        .order_by(desc(Course.created_at)) \
        .paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
