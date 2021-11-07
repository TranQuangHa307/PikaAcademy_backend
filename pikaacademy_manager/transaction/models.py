# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Enum, ForeignKey, Integer, String, Text, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR
from sqlalchemy.orm import relationship
from libs.sql_action import Base
from flask_restx import fields
transaction_fields = {
  "user_id": fields.Integer(required=True),
  "first_name": fields.String(required=True),
  "last_name": fields.String(required=True),
  "email": fields.String(required=True),
  "phone_number": fields.String(required=True),
  "voucher_id": fields.Integer(required=True),
  "discount": fields.Integer(required=True),
  "total": fields.Arbitrary(required=True),
  "payment_mode": fields.Integer(required=True),
  "status": fields.String(),
  "transaction_course": fields.List(fields.Raw()),
}
transaction_change_fields = {
  "user_id": fields.Integer(),
  "status": fields.String(),
  "cart_id": fields.Integer(),
  "transaction_course": fields.List(fields.Raw()),
}


class Transaction(Base):
  __tablename__ = 'transaction'
  id = Column(INTEGER, primary_key=True)
  code = Column(String(36),  server_default=text("(uuid())"))
  user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
  first_name = Column(VARCHAR(256), nullable=False)
  last_name = Column(VARCHAR(256), nullable=False)
  email = Column(VARCHAR(256), nullable=False)
  phone_number = Column(String(11))
  voucher_id = Column(INTEGER)
  discount = Column(Integer, server_default=text("'0'"))
  total = Column(DECIMAL(10, 0), nullable=False)
  payment_mode = Column(Enum('bank', 'paypal'))
  time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
  status = Column(Enum('initial', 'canceled', 'pending', 'success'))
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  user = relationship('User')

  def __init__(self, params):
    self.user_id = params["user_id"]
    self.first_name = params["first_name"]
    self.last_name = params["last_name"]
    self.email = params["email"]
    self.phone_number = params["phone_number"]
    self.voucher_id = params["voucher_id"]
    self.discount = params["discount"]
    self.total = params["total"]
    self.payment_mode = params["payment_mode"]
    self.status = params["status"]


class TransactionCourse(Base):
  __tablename__ = 'transaction_course'

  id = Column(INTEGER, primary_key=True)
  transaction_id = Column(ForeignKey('transaction.id'), nullable=False, index=True)
  course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
  course_name = Column(Text, nullable=False)
  price_id = Column(ForeignKey('price.id'), nullable=False, index=True)
  original_price = Column(DECIMAL(10, 0), nullable=False)
  discount_promotion_id = Column(ForeignKey('discount_promotion.id'), index=True)
  discount = Column(Integer, server_default=text("'0'"))
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  course = relationship('Course')
  discount_promotion = relationship('DiscountPromotion')
  price = relationship('Price')
  transaction = relationship('Transaction')

  def __init__(self, params):
    self.transaction_id = params["transaction_id"]
    self.course_id = params["course_id"]
    self.course_name = params["course_name"]
    self.price_id = params["price_id"]
    self.original_price = params["original_price"]
    self.discount_promotion_id = params["discount_promotion_id"]
    self.discount = params["discount"]
