# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, String, Text, text, ForeignKey
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR
from libs.sql_action import Base
from flask_restx import fields
from sqlalchemy.orm import relationship

user_fields = {
  "first_name": fields.String(required=True),
  "last_name": fields.String(required=True),
  "email": fields.String(required=True),
  "url_avatar": fields.String(required=True),
  "date_of_birth": fields.DateTime(),
  "gender": fields.String(),
  "phone_number": fields.String(),
  "hash_pwd": fields.String()
}

user_like_course_fields = {
  "user_id": fields.Integer(required=True),
  "course_id": fields.Integer(required=True),
}

user_purchase_course_fields = {
  "user_id": fields.Integer(required=True),
  "course_id": fields.Integer(required=True),
  "transaction_id": fields.Integer(required=True),
}


class User(Base):
  __tablename__ = 'user'

  id = Column(INTEGER, primary_key=True)
  first_name = Column(VARCHAR(256), nullable=False)
  last_name = Column(VARCHAR(256), nullable=False)
  email = Column(VARCHAR(256), nullable=False)
  url_avatar = Column(Text, nullable=False)
  date_of_birth = Column(DateTime)
  gender = Column(Enum('not_specific', 'male', 'female'), nullable=False, server_default=text("'not_specific'"))
  phone_number = Column(String(11))
  hash_pwd = Column(VARCHAR(256))
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  def __init__(self, params):
    self.first_name = params["first_name"]
    self.last_name = params["last_name"]
    self.email = params["email"]
    self.url_avatar = params["url_avatar"]
    self.date_of_birth = params["date_of_birth"]
    self.gender = params["gender"]
    self.phone_number = params["phone_number"]
    self.hash_pwd = params["hash_pwd"]


class UserLikeCourse(Base):
  __tablename__ = 'user_like_course'

  id = Column(INTEGER, primary_key=True)
  user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
  course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
  time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  def __init__(self, params):
    self.user_id = params["user_id"]
    self.course_id = params["course_id"]


class UserPurchaseCourse(Base):
  __tablename__ = 'user_purchase_course'

  id = Column(INTEGER, primary_key=True)
  user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
  course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
  transaction_id = Column(ForeignKey('transaction.id'), nullable=False, index=True)
  time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  course = relationship('Course')
  # transaction = relationship('Transaction')
  user = relationship('User')

  def __init__(self, params):
    self.user_id = params["user_id"]
    self.course_id = params["course_id"]
    self.transaction_id = params["transaction_id"]
