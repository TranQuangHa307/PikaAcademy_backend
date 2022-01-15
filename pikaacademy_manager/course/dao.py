import datetime
from logging import getLogger

from category.models import Category
from common.models import Pagination
from interests.models import Interests
from libs.sql_action import db, safe_commit
from sqlalchemy import desc, and_, or_
from teacher.models import Teacher
from user.models import UserLikeCourse, UserPurchaseCourse
from werkzeug.exceptions import InternalServerError

from .models import Course, Price, DiscountPromotion, Material

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
        Course.created_at,
        Course.updated_at,
        Course.is_active,
        Course.release,
        Teacher.full_name.label('teacher_name'),
        Interests.name.label('interest_name'),
        Category.name.label('category_name'),
        Price.price.label('price'),
        DiscountPromotion.discount.label('discount'),
        UserLikeCourse.id.label('user_like_course_id'),
        UserPurchaseCourse.id.label('user_purchase_course_id')
      ).join(Interests, Interests.id == Course.interests_id) \
        .join(Category, Category.id == Course.category_id) \
        .outerjoin(Price,
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
      else:
        res_query = res_query.join(Teacher, Teacher.id == Course.teacher_id)
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
              res_query = res_query.filter(Price.price == 0)
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
  def get_all_inactive():
    try:
      res_query = db.session.query(
        Course.id,
        Course.name
      ).filter(Course.deleted_flag.isnot(True), Course.is_active, Course.release.isnot(True))
      res_query = res_query.order_by(Course.updated_at).all()
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
      Course.rating,
      Course.is_active,
      Course.release,
      Price.id.label('price_id'),
      Price.price.label('price'),
      DiscountPromotion.id.label('discount_promotion_id'),
      DiscountPromotion.discount.label('discount'),
      DiscountPromotion.begin_date.label('discount_begin_date'),
      DiscountPromotion.end_date.label('discount_end_date'),
      UserLikeCourse.id.label('user_like_course_id'),
      UserPurchaseCourse.id.label('user_purchase_course_id'),
      UserPurchaseCourse.is_rating.label('user_purchase_course_is_rating'),
      Category.name.label('category_name'),
      Interests.name.label('interests_name'),
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

  @staticmethod
  def update_purchases(course_ids):
    try:
      db.session.query(Course).filter(Course.id.in_(course_ids),
                                      Course.deleted_flag.isnot(True)).update(
        dict(purchases=(Course.purchases + 1)))
      safe_commit()
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


class CourseTeacherDAO(object):
  @staticmethod
  def get_top_course_by_teacher_id(teacher_id, status):
    try:
      res_query = db.session.query(
        Course.id,
        Course.name,
        Course.url_image,
        Course.likes,
        Course.purchases
      ).filter(Course.teacher_id == teacher_id,
               Course.deleted_flag.isnot(True))
      if status == 'like':
        res_query = res_query.order_by(desc(Course.likes))
      if status == 'purchases':
        res_query = res_query.order_by(desc(Course.purchases))
      if status == 'rating':
        res_query = res_query.join(Rating, Rating.cour)
      res_query = res_query.group_by(Course.id).limit(5).all()
      return res_query
    except Exception:
      raise InternalServerError()


class PriceDAO(object):

  @staticmethod
  def get_list_by_course_id(course_id):
    try:
      res_query = db.session.query(
        Price.id,
        Price.created_at,
        Price.price
      ).filter(Price.course_id == course_id, Price.deleted_flag.isnot(True)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        Price.id,
        Price.price,
        Price.course_id,
        Price.is_active
      ).filter(Price.id == _id, Price.deleted_flag.isnot(True)).first()
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
  def get_list_by_course_id(course_id):
    try:
      res_query = db.session.query(
        DiscountPromotion.id,
        DiscountPromotion.discount,
        DiscountPromotion.begin_date,
        DiscountPromotion.end_date,
      ).filter(DiscountPromotion.course_id, DiscountPromotion.deleted_flag.isnot(True)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        DiscountPromotion.id,
        DiscountPromotion.discount,
        DiscountPromotion.begin_date,
        DiscountPromotion.end_date,
        DiscountPromotion.is_active
      ).filter(DiscountPromotion.id == _id, DiscountPromotion.deleted_flag.isnot(True)).first()
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


class MaterialDAO(object):
  @staticmethod
  def get_list_by_course_id(course_id):
    try:
      res_query = db.session.query(
        Material.id,
        Material.name,
        Material.link,
        Material.course_id
      ).filter(Material.course_id == course_id,
               Material.deleted_flag.isnot(True))
      res_query = res_query.group_by(Material.id).order_by(Material.created_at).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def bulk_add(material_arr):
    try:
      material_sql = []
      for item in material_arr:
        material = Material(item)
        material_sql.append(material)
      if material_sql:
        db.session.bulk_save_objects(material_sql)
        safe_commit()
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def clear_by_course_id(course_id):
    try:
      db.session.query(Material).filter(Material.course_id == course_id,
                                        Material.deleted_flag.isnot(True)).update(
        dict(deleted_flag=1))
      safe_commit()
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
