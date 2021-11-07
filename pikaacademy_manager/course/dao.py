from libs.sql_action import db
from category.models import Category
from interests.models import Interests
from werkzeug.exceptions import InternalServerError
from sqlalchemy import desc, and_, or_
from teacher.models import Teacher
from .models import Course, Price, DiscountPromotion
from user.models import UserLikeCourse, UserPurchaseCourse
from common.models import Pagination
import datetime
from logging import getLogger

logger = getLogger(__name__)


class CourseDAO(object):
  @staticmethod
  def get_list(args: Pagination):
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
        Price.price.label('price'),
        DiscountPromotion.discount.label('discount'),
        UserLikeCourse.id.label('user_like_course_id'),
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
        .outerjoin(UserLikeCourse,
                   and_(UserLikeCourse.course_id == Course.id,
                        UserLikeCourse.user_id == args.user_id,
                        UserLikeCourse.deleted_flag.isnot(True))) \
        .outerjoin(UserPurchaseCourse,
                   and_(UserPurchaseCourse.course_id == Course.id,
                        UserPurchaseCourse.user_id == args.user_id,
                        UserPurchaseCourse.deleted_flag.isnot(True))).filter(
        Course.deleted_flag.isnot(True))
      if args.teacher_id:
        logger.info(f'teacher_id: {args.teacher_id}')
        res_query = res_query.join(Teacher,
                                   and_(Teacher.id == Course.teacher_id,
                                        Teacher.id == args.teacher_id,
                                        Teacher.deleted_flag.isnot(True)))
      if args.keyword:
        res_query = res_query.filter(Course.name.ilike(f'%{args.keyword}%'))
      if args.interests:
        res_query = res_query.filter(Course.interests_id.in_(args.interests))
      if args.categories:
        res_query = res_query.filter(Course.category_id.in_(args.categories))
      if args.prices:
        if len(args.prices) > 1:
          res_query = res_query.filter(or_(Price.price == 0, DiscountPromotion.discount))
        else:
          for item in args.prices:
            if item == 'free':
              res_query = res_query.filter(Price.price==0)
            if item == 'discount':
              res_query = res_query.filter(DiscountPromotion.discount)
      if args.levels:
        res_query = res_query.filter(Course.level.in_(args.levels))
      if args.type == 'purchases':
        res_query = res_query.order_by(desc(Course.purchases))
      elif args.type == 'like':
        res_query = res_query.order_by(desc(Course.likes))
      else:
        res_query = res_query.order_by(desc(Course.created_at))
      res_query = res_query.paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_list_by_type(args: Pagination):
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
        Price.id.label('price_id'),
        Price.price.label('price'),
        DiscountPromotion.id.label('discount_promotion_id'),
        DiscountPromotion.discount.label('discount'),
        UserLikeCourse.id.label('user_like_course_id'),
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
        .outerjoin(UserLikeCourse,
                   and_(UserLikeCourse.course_id == Course.id,
                        UserLikeCourse.user_id == args.user_id,
                        UserLikeCourse.deleted_flag.isnot(True))) \
        .outerjoin(UserPurchaseCourse,
                   and_(UserPurchaseCourse.course_id == Course.id,
                        UserPurchaseCourse.user_id == args.user_id,
                        UserPurchaseCourse.deleted_flag.isnot(True))) \
        .filter(Course.deleted_flag.isnot(True))
      logger.info(f'args: {args.type}')
      if args.type == 'purchases':
        res_query = res_query.order_by(desc(Course.purchases))
      elif args.type == 'like':
        res_query = res_query.order_by(desc(Course.likes))
      else:
        res_query = res_query.order_by(desc(Course.created_at))
      res_query = res_query.paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_id(_id, user_id=0):
    current_date = datetime.datetime.now()
    logger.info(f'current_date: {current_date}')
    res_query = db.session.query(
      Course.id,
      Course.name,
      Course.description,
      Course.about,
      Course.url_image,
      Course.url_intro_video,
      Course.result,
      Course.level,
      Course.views,
      Course.likes,
      Course.purchases,
      Course.created_at,
      Course.updated_at,
      Course.interests_id,
      Course.category_id,
      Course.teacher_id,
      Price.id.label('price_id'),
      Price.price.label('price'),
      DiscountPromotion.id.label('discount_promotion_id'),
      DiscountPromotion.discount.label('discount'),
      DiscountPromotion.begin_date.label('discount_begin_date'),
      DiscountPromotion.end_date.label('discount_end_date'),
      UserLikeCourse.id.label('user_like_course_id'),
      UserPurchaseCourse.id.label('user_purchase_course_id'),
      Category.name.label('category_name'),
      Interests.name.label('interests_name')
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
      .outerjoin(UserLikeCourse,
                 and_(UserLikeCourse.course_id == Course.id,
                      UserLikeCourse.user_id == user_id,
                      UserLikeCourse.deleted_flag.isnot(True))) \
      .outerjoin(UserPurchaseCourse,
                 and_(UserPurchaseCourse.course_id == Course.id,
                      UserPurchaseCourse.user_id == user_id,
                      UserPurchaseCourse.deleted_flag.isnot(True))) \
      .join(Category, and_(Category.id == Course.category_id, Category.deleted_flag.isnot(True))) \
      .join(Interests, and_(Interests.id == Course.interests_id, Interests.deleted_flag.isnot(True))) \
      .filter(Course.id == _id, Course.deleted_flag.isnot(True)).first()
    return res_query

  @staticmethod
  def add(params):
    try:
      course = Course(params)
      Course.create(course)
      return course.id
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update(course_id, data_dict):
    try:
      Course.update(course_id, data_dict)
    except Exception:
      raise InternalServerError()

  @staticmethod
  def delete(course_id):
    try:
      Course.update(course_id, {"deleted_flag": True})
    except Exception:
      raise InternalServerError()

class PriceDAO(object):

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        Price.id,
        Price.price,
        Price.course_id,
        Price.is_active
      ).filter(Price.id==_id, Price.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def inactive(_id):
    try:
      Price.update(_id, {"is_active": False})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      price = Price(params)
      Price.create(price)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

class DiscountPromotionDAO(object):

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        DiscountPromotion.id,
        DiscountPromotion.discount,
        DiscountPromotion.begin_date,
        DiscountPromotion.end_date,
        DiscountPromotion.is_active
      ).filter(DiscountPromotion.id==_id, DiscountPromotion.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def inactive(_id):
    try:
      DiscountPromotion.update(_id, {"is_active": False})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      discount_promotion = DiscountPromotion(params)
      DiscountPromotion.create(discount_promotion)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

