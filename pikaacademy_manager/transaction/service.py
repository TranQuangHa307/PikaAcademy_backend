from user.dao import UserPurchaseCourseDAO
from course.dao import CourseDAO
from werkzeug.exceptions import InternalServerError
from logging import getLogger
from common.constants import TransactionStatusEnum
from common.mail.send_mail import (transfer_successful)
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
          "discount": item["discount"] if item["discount"] else 0,
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
      course_ids = [el['course_id'] for el in transaction_courses]
      if user_purchase_courses and transaction_db.status == TransactionStatusEnum.Success.value:
        UserPurchaseCourseDAO.bulk_add(user_purchase_courses)
        logger.info(f'transaction_courses = {transaction_courses}')
        transfer_successful(email=params['email'], full_name=f"{params['first_name']} {params['last_name']}", transaction=transaction_db, transaction_courses=transaction_courses)
        CourseDAO.update_purchases(course_ids)
      if transaction_db.status != TransactionStatusEnum.Initial.value and params["payment_mode"] and params["cart_id"]:
        CartCourseDAO.clear_by_cart(cart_id=params["cart_id"], course_ids=course_ids)
      return transaction_db.id
  except Exception as e:
    raise InternalServerError(str(e.__cause__))

def update_transaction_status(transaction_id, params):
  try:
    TransactionDAO.update(transaction_id, {"status": params["status"]})
    transaction_db = TransactionDAO.get_by_id(transaction_id)
    if transaction_db.status == TransactionStatusEnum.Canceled.value:
      return
    course_ids = [el['course_id'] for el in params["transaction_course"]]
    if transaction_db.status != TransactionStatusEnum.Initial.value and params["cart_id"]:
      CartCourseDAO.clear_by_cart(cart_id=params["cart_id"], course_ids=course_ids)
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
        transaction_course_db = TransactionCourseDAO.get_list_by_transaction(transaction_db.id)
        transfer_successful(email=transaction_db.email, full_name=f"{transaction_db.first_name} {transaction_db.last_name}",
                            transaction=transaction_db, transaction_courses=transaction_course_db)
        UserPurchaseCourseDAO.bulk_add(user_purchase_courses)
        CourseDAO.update_purchases(course_ids)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
