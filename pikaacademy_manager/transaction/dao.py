from libs.sql_action import db, safe_commit
from .models import Transaction, TransactionCourse
from werkzeug.exceptions import InternalServerError
from logging import getLogger
from sqlalchemy import desc
from common.models import Pagination
from common.constants import TransactionStatusEnum
logger = getLogger(__name__)


class TransactionDAO(object):
  @staticmethod
  def get_list(args: Pagination):
    try:
      res_query = db.session.query(
        Transaction.id,
        Transaction.code,
        Transaction.user_id,
        Transaction.first_name,
        Transaction.last_name,
        Transaction.email,
        Transaction.phone_number,
        Transaction.voucher_id,
        Transaction.discount,
        Transaction.total,
        Transaction.payment_mode,
        Transaction.status,
        Transaction.time
      )
      if args.status:
        res_query = res_query.filter(Transaction.status == args.status)
      res_query = res_query.filter(Transaction.deleted_flag.isnot(True))\
        .group_by(Transaction.id).order_by(desc(Transaction.created_at)) \
        .paginate(args.page, args.limit)
      return res_query
    except Exception as e:
      raise InternalServerError(e.__cause__)

  @staticmethod
  def get_by_id(_id):
    try:
      res_query = db.session.query(
        Transaction.id,
        Transaction.code,
        Transaction.user_id,
        Transaction.first_name,
        Transaction.last_name,
        Transaction.email,
        Transaction.phone_number,
        Transaction.voucher_id,
        Transaction.discount,
        Transaction.total,
        Transaction.payment_mode,
        Transaction.status,
        Transaction.time
      ).filter(Transaction.id == _id, Transaction.deleted_flag.isnot(True)).first()
      return res_query
    except Exception as e:
      raise InternalServerError(e.__cause__)

  @staticmethod
  def get_list_by_status(status):
    try:
      res_query = db.session.query(
        Transaction.id,
        Transaction.code,
        Transaction.user_id,
        Transaction.first_name,
        Transaction.last_name,
        Transaction.email,
        Transaction.phone_number,
        Transaction.voucher_id,
        Transaction.discount,
        Transaction.total,
        Transaction.payment_mode,
        Transaction.status,
        Transaction.time
      ).filter(Transaction.deleted_flag.isnot(True), Transaction.status==status).all()
      return res_query
    except Exception as e:
      raise InternalServerError(e.__cause__)

  @staticmethod
  def add(params):
    try:
      transaction = Transaction(params)
      logger.info(f'transaction: {transaction}')
      Transaction.create(transaction)
      return transaction
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update(_id, data_dict):
    try:
      Transaction.update(_id, data_dict)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))


class TransactionCourseDAO(object):
  @staticmethod
  def bulk_add(transaction_courses):
    try:
      transaction_courses_sql = []
      for item in transaction_courses:
        transaction_course = TransactionCourse(item)
        transaction_courses_sql.append(transaction_course)
      db.session.bulk_save_objects(transaction_courses_sql)
      safe_commit()
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def get_list_by_transaction(transaction_id):
    try:
      res_query = db.session.query(
        TransactionCourse.id,
        TransactionCourse.course_id,
        TransactionCourse.course_name,
        TransactionCourse.price_id,
        TransactionCourse.original_price,
        TransactionCourse.discount_promotion_id,
        TransactionCourse.discount
      ).filter(TransactionCourse.transaction_id == transaction_id, TransactionCourse.deleted_flag.isnot(True)).order_by(
        desc(TransactionCourse.created_at)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
