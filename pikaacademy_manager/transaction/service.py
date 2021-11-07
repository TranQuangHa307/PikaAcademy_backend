from user.dao import UserPurchaseCourseDAO
from course.dao import CourseDAO
from werkzeug.exceptions import InternalServerError
from logging import getLogger
from common.constants import TransactionStatusEnum
from .dao import TransactionDAO, TransactionCourseDAO
from cart.dao import CartCourseDAO
logger = getLogger(__name__)


def transaction(params):
  try:
    transaction_obj = {
      "user_id": params["user_id"],
      "first_name": params["first_name"],
      "last_name": params["last_name"],
      "email": params["email"],
      "phone_number": params["phone_number"],
      "voucher_id": params["voucher_id"],
      "discount": params["discount"],
      "total": params["total"],
      "payment_mode": params["payment_mode"],
      "status": params["status"],
    }
    transaction_db = TransactionDAO.add(transaction_obj)
    if not transaction_db:
      return None
    else:
      transaction_courses = []
      user_purchase_courses = []
      for item in params["transaction_course"]:
        transaction_course_obj = {
          "transaction_id": transaction_db.id,
          "course_id": item["course_id"],
          "course_name": item["course_name"],
          "price_id": item["price_id"],
          "original_price": item["price"],
          "discount_promotion_id": item["discount_promotion_id"],
          "discount": item["discount"],
        }
        user_purchase_course_obj = {
          "user_id": params["user_id"],
          "course_id": item["course_id"],
          "transaction_id": transaction_db.id,
        }
        transaction_courses.append(transaction_course_obj)
        user_purchase_courses.append(user_purchase_course_obj)
      if transaction_courses:
        TransactionCourseDAO.bulk_add(transaction_courses)
      if user_purchase_courses and transaction_db.status == TransactionStatusEnum.Success.value:
        UserPurchaseCourseDAO.bulk_add(user_purchase_courses)
      if transaction_db.status != TransactionStatusEnum.Initial.value and params["payment_mode"] and params["cart_id"]:
        CartCourseDAO.clear_by_cart(params["cart_id"])
      return transaction_db.id
  except Exception as e:
    raise InternalServerError(str(e.__cause__))

def update_transaction_status(transaction_id, params):
  try:
    TransactionDAO.update(transaction_id, {"status": params["status"]})
    transaction_db = TransactionDAO.get_by_id(transaction_id)
    if transaction_db.status != TransactionStatusEnum.Initial.value and params["cart_id"]:
      CartCourseDAO.clear_by_cart(params["cart_id"])
    if transaction_db.status == TransactionStatusEnum.Success.value:
      user_purchase_courses = []
      for item in params["transaction_course"]:
        user_purchase_course_obj = {
          "user_id": params["user_id"],
          "course_id": item["course_id"],
          "transaction_id": transaction_db.id,
        }
        user_purchase_courses.append(user_purchase_course_obj)
      if user_purchase_courses and transaction_db.status == TransactionStatusEnum.Success.value:
        UserPurchaseCourseDAO.bulk_add(user_purchase_courses)
        for item in user_purchase_courses:
          course = CourseDAO.get_by_id(item["course_id"])
          purchases = course.purchases + 1
          CourseDAO.update(course.id, {'purchases': purchases})
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
