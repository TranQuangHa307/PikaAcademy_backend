import datetime

from common.models import Pagination
from course.models import Course, Price, DiscountPromotion
from libs.sql_action import db, safe_commit
from sqlalchemy import desc, or_, and_, func
from teacher.models import Teacher
from transaction.models import Transaction, TransactionCourse
from werkzeug.exceptions import InternalServerError
from werkzeug.security import generate_password_hash

from .models import User, UserLikeCourse, UserPurchaseCourse


class UserDAO(object):
  @staticmethod
  def get_list(args: Pagination):
    try:
      res_query = db.session.query(
        User.id,
        User.first_name,
        User.last_name,
        User.email,
        User.url_avatar,
        User.date_of_birth,
        User.gender,
        User.phone_number
      ).filter(User.deleted_flag.isnot(True))
      if args.keyword:
        res_query = res_query.filter(or_(User.first_name.ilike(f'%{args.keyword}%'),
                                         User.last_name.ilike(f'%{args.keyword}%')))
      res_query = res_query.group_by(User.id).order_by(desc(User.created_at)).paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        User.id,
        User.first_name,
        User.last_name,
        User.email,
        User.url_avatar,
        User.date_of_birth,
        User.gender,
        User.phone_number
      ).filter(User.deleted_flag.isnot(True),
               User.id == _id).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_email(email):
    try:
      res_query = db.session.query(
        User.id,
        User.first_name,
        User.last_name,
        User.email,
        User.url_avatar,
        User.date_of_birth,
        User.gender,
        User.phone_number,
        User.hash_pwd
      ).filter(User.deleted_flag.isnot(True),
               User.email == email).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      user = User(params)
      if not user.hash_pwd:
        user.hash_pwd = 'Aa123456@'
      user.hash_pwd = generate_password_hash(user.hash_pwd)
      User.create(user)
      return user
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update(_id, data_dict):
    try:
      User.update(_id, data_dict)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def delete(_id):
    try:
      User.update(_id, {"delete_flag": True})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


class UserLikeCourseDAO(object):

  @staticmethod
  def get_list_by_course_id(args: Pagination, course_id):
    try:
      res_query = db.session.query(
        UserLikeCourse.id,
        UserLikeCourse.course_id,
        UserLikeCourse.user_id,
        UserLikeCourse.time,
        User.first_name.label('user_first_name'),
        User.last_name.label('user_last_name'),
        User.url_avatar.label('user_url_avatar')
      ).join(User, User.id == UserLikeCourse.user_id) \
        .filter(UserLikeCourse.course_id == course_id,
                UserLikeCourse.deleted_flag.isnot(True))
      res_query = res_query.order_by(desc(UserLikeCourse.time)).paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_id(course_id, user_id):
    try:
      res_query = db.session.query(
        UserLikeCourse.id,
        UserLikeCourse.course_id,
        UserLikeCourse.user_id,
        UserLikeCourse.time
      ).filter(UserLikeCourse.course_id == course_id,
               UserLikeCourse.user_id == user_id,
               UserLikeCourse.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_list(args: Pagination, _id):
    try:
      current_date = datetime.datetime.now()
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
        Course.created_at,
        Course.updated_at,
        Price.price.label('price'),
        DiscountPromotion.discount.label('discount'),
        UserLikeCourse.id.label('user_like_course_id'),
        UserLikeCourse.time.label('liked_at'),
        UserPurchaseCourse.id.label('user_purchase_course_id')
      ).outerjoin(Price,
                  and_(Price.course_id == Course.id,
                       Price.is_active == 1,
                       Price.deleted_flag.isnot(True))) \
        .outerjoin(DiscountPromotion,
                   and_(DiscountPromotion.course_id == Course.id,
                        DiscountPromotion.is_active == 1,
                        DiscountPromotion.begin_date <= current_date,
                        DiscountPromotion.end_date >= current_date,
                        DiscountPromotion.deleted_flag.isnot(True))) \
        .join(UserLikeCourse, UserLikeCourse.course_id == Course.id) \
        .outerjoin(UserPurchaseCourse,
                   and_(UserPurchaseCourse.course_id == Course.id,
                        UserPurchaseCourse.user_id == _id,
                        UserPurchaseCourse.deleted_flag.isnot(True))) \
        .filter(UserLikeCourse.user_id == _id,
                UserLikeCourse.deleted_flag.isnot(True),
                Course.deleted_flag.isnot(True))
      res_query = res_query.order_by(desc(UserLikeCourse.time)).paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      user_like_course = UserLikeCourse(params)
      UserLikeCourse.create(user_like_course)
      return user_like_course.id
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def delete(_id):
    try:
      UserLikeCourse.update(_id, {"deleted_flag": True})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


class UserPurchaseCourseDAO(object):
  @staticmethod
  def get_list(args: Pagination, _id):
    try:
      current_date = datetime.datetime.now()
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
        Course.created_at,
        Course.updated_at,
        Price.price.label('price'),
        DiscountPromotion.discount.label('discount'),
        UserLikeCourse.id.label('user_like_course_id'),
        UserPurchaseCourse.id.label('user_purchase_course_id'),
        TransactionCourse.original_price.label('transaction_original_price'),
        TransactionCourse.discount.label('transaction_discount'),
        Transaction.time.label('transaction_time'),
        Teacher.full_name.label('teacher')
      ).outerjoin(Price,
                  and_(Price.course_id == Course.id,
                       Price.is_active == 1,
                       Price.deleted_flag.isnot(True))) \
        .outerjoin(DiscountPromotion,
                   and_(DiscountPromotion.course_id == Course.id,
                        DiscountPromotion.is_active == 1,
                        DiscountPromotion.begin_date <= current_date,
                        DiscountPromotion.end_date >= current_date,
                        DiscountPromotion.deleted_flag.isnot(True))) \
        .join(Teacher, Teacher.id == Course.teacher_id) \
        .join(UserPurchaseCourse, UserPurchaseCourse.course_id == Course.id) \
        .join(Transaction, Transaction.id == UserPurchaseCourse.transaction_id) \
        .join(TransactionCourse, and_(TransactionCourse.transaction_id == Transaction.id,
                                      TransactionCourse.course_id == Course.id)) \
        .outerjoin(UserLikeCourse, and_(UserLikeCourse.course_id == Course.id,
                                        UserLikeCourse.user_id == _id,
                                        UserLikeCourse.deleted_flag.isnot(True))) \
        .filter(UserPurchaseCourse.user_id == _id,
                UserPurchaseCourse.deleted_flag.isnot(True),
                Course.deleted_flag.isnot(True))
      res_query = res_query.order_by(desc(UserPurchaseCourse.time)).paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      user_purchase_course = UserPurchaseCourse(params)
      UserPurchaseCourse.create(user_purchase_course)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update_is_rating(_id):
    try:
      UserPurchaseCourse.update(_id, {"is_rating": True})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def bulk_add(user_purchase_courses):
    try:
      user_purchase_courses_sql = []
      for item in user_purchase_courses:
        user_purchase_course = UserPurchaseCourse(item)
        user_purchase_courses_sql.append(user_purchase_course)
      db.session.bulk_save_objects(user_purchase_courses_sql)
      safe_commit()
    except Exception as e:
      raise InternalServerError(e.__cause__)

  @staticmethod
  def get_user_total_by_teacher_id(teacher_id):
    try:
      res_query = db.session.query(Course.teacher_id, func.count(UserPurchaseCourse.user_id).label('total')) \
        .join(UserPurchaseCourse, UserPurchaseCourse.course_id == Course.id) \
        .filter(Course.teacher_id == teacher_id,
                Course.deleted_flag.isnot(True),
                UserPurchaseCourse.deleted_flag.isnot(True)).group_by(UserPurchaseCourse.user_id).first()
      return res_query
    except Exception as e:
      raise InternalServerError(e.__cause__)


class UserByCourse(object):
  @staticmethod
  def get_list_by_course_id(args: Pagination, course_id):
    try:
      res_query = db.session.query(
        User.id,
        User.first_name,
        User.last_name,
        User.email,
        User.date_of_birth,
        User.url_avatar,
        Transaction.time.label('buyed_at')
      ).join(Transaction, Transaction.user_id == User.id) \
        .join(TransactionCourse, TransactionCourse.transaction_id == Transaction.id) \
        .filter(TransactionCourse.course_id == course_id,
                Transaction.status == 'success',
                TransactionCourse.deleted_flag.isnot(True),
                Transaction.deleted_flag.isnot(True),
                User.deleted_flag.isnot(True))
      res_query = res_query.order_by(desc(Transaction.created_at)).paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_all_by_course_id(course_id):
    try:
      res_query = db.session.query(
        User.id,
        User.first_name,
        User.last_name,
        User.email,
        User.date_of_birth,
        User.url_avatar,
        Transaction.time.label('buyed_at')
      ).join(Transaction, Transaction.user_id == User.id) \
        .join(TransactionCourse, TransactionCourse.transaction_id == Transaction.id) \
        .filter(TransactionCourse.course_id == course_id,
                Transaction.status == 'success',
                TransactionCourse.deleted_flag.isnot(True),
                Transaction.deleted_flag.isnot(True),
                User.deleted_flag.isnot(True))
      res_query = res_query.order_by(desc(Transaction.created_at)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


class CourseTeacherDAO(object):
  @staticmethod
  def get_top_course_by_teacher_id(teacher_id, keyword):
    try:
      res_query = db.session.query(
        Course.id,
        Course.name,
        Course.url_image,
        Course.likes,
        Course.purchases
      ).filter(Course.teacher_id == teacher_id,
               Course.deleted_flag.isnot(True))
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
