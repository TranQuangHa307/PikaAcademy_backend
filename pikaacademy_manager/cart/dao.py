import datetime
from common.models import Pagination
from course.models import Course, Price, DiscountPromotion
from libs.sql_action import db, safe_commit
from sqlalchemy import desc, and_, func
from werkzeug.exceptions import InternalServerError

from .models import Cart, CartCourse


class CartDAO(object):
  @staticmethod
  def get_by_user_id(user_id):
    try:
      res_query = db.session.query(
        Cart.id,
        Cart.user_id,
        func.count(CartCourse.id).label('cart_count')
      ).outerjoin(CartCourse, and_(CartCourse.cart_id == Cart.id, CartCourse.deleted_flag.isnot(True))).filter(
        Cart.user_id == user_id,
        Cart.deleted_flag.isnot(True)).group_by(Cart.id).first()
      return res_query
    except Exception as e:
      raise InternalServerError(e.__cause__)

  @staticmethod
  def add(params):
    try:
      cart = Cart(params)
      Cart.create(cart)
    except Exception as e:
      raise InternalServerError(e.__cause__)


class CartCourseDAO(object):
  @staticmethod
  def get_by_course_and_cart(course_id, cart_id):
    try:
      res_query = db.session.query(
        CartCourse.id,
        CartCourse.cart_id,
        CartCourse.course_id
      ).filter(CartCourse.cart_id == cart_id,
               CartCourse.course_id == course_id,
               CartCourse.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(e.__cause__)

  @staticmethod
  def get_list_by_cart_id(cart_id):
    try:
      current_date = datetime.datetime.now()
      res_query = db.session.query(
        CartCourse.id,
        CartCourse.cart_id,
        CartCourse.course_id,
        Course.id.label('course_id'),
        Course.name.label('course_name'),
        Course.url_image.label('url_image'),
        Price.id.label('price_id'),
        Price.price.label('price'),
        DiscountPromotion.id.label('discount_promotion_id'),
        DiscountPromotion.discount.label('discount'),
      ).join(Course,
             and_(Course.id == CartCourse.course_id,
                  Course.deleted_flag.isnot(True))) \
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
        .filter(CartCourse.cart_id == cart_id,
                CartCourse.deleted_flag.isnot(True))
      res_query = res_query.order_by(desc(CartCourse.created_at)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      cart_course = CartCourse(params)
      CartCourse.create(cart_course)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def delete(_id):
    try:
      CartCourse.update(_id, {"deleted_flag": True})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def clear_by_cart(cart_id, course_ids):
    try:
      db.session.query(CartCourse).filter(CartCourse.cart_id == cart_id,
                                          CartCourse.course_id.in_(course_ids),
                                          CartCourse.deleted_flag.isnot(True)).update(
        dict(deleted_flag=1))
      safe_commit()
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
