# coding: utf-8
from common.models import NullableString, NullableInteger
from flask_restx import fields
from libs.sql_action import Base
from sqlalchemy import Column, DECIMAL, DateTime, Enum, Integer, Text, text, ForeignKey
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR

course_fields = {
  "name": fields.String(required=True),
  "description": fields.String(required=True),
  "about": fields.String(required=True),
  "url_image": fields.String(required=True),
  "url_intro_video": fields.String(required=True),
  "result": fields.String(required=True),
  "level": fields.String(required=True),
  "price_id": NullableInteger,
  "price": fields.Arbitrary(min=0, required=True),
  "discount_promotion_id": NullableInteger,
  "discount": NullableInteger,
  "begin_date": NullableString,
  "end_date": NullableString,
  "interests_id": fields.Integer(required=True),
  "category_id": fields.Integer(required=True),
  "teacher_id": fields.Integer(required=True),
  "created_by": fields.String(required=True),
  "updated_by": fields.String(required=True),
  "material": fields.List(fields.Raw())
}


class Course(Base):
  __tablename__ = 'course'

  id = Column(INTEGER, primary_key=True)
  name = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  about = Column(Text, nullable=False)
  url_image = Column(Text, nullable=False)
  url_intro_video = Column(Text, nullable=False)
  result = Column(Text, nullable=False)
  level = Column(Enum('beginner', 'intermediate', 'advance'), nullable=False)
  views = Column(Integer, nullable=False, server_default=text("'0'"))
  likes = Column(Integer, nullable=False, server_default=text("'0'"))
  rating = Column(Integer, nullable=False, server_default=text("'0'"))
  purchases = Column(Integer, nullable=False, server_default=text("'0'"))
  is_active = Column(BIT(1))
  release = Column(BIT(1))
  interests_id = Column(ForeignKey('interests.id'), nullable=False, index=True)
  category_id = Column(ForeignKey('category.id'), nullable=False, index=True)
  teacher_id = Column(ForeignKey('teacher.id'), nullable=False, index=True)
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  created_by = Column(VARCHAR(256), nullable=False)
  updated_by = Column(VARCHAR(256), nullable=False)
  deleted_flag = Column(BIT(1))

  def __init__(self, params):
    self.name = params["name"]
    self.description = params["description"]
    self.about = params["about"]
    self.url_image = params['url_image']
    self.url_intro_video = params["url_intro_video"]
    self.result = params["result"]
    self.level = params["level"]
    self.interests_id = params["interests_id"]
    self.category_id = params["category_id"]
    self.teacher_id = params["teacher_id"]
    self.created_by = params["created_by"]
    self.updated_by = params["updated_by"]


class Material(Base):
  __tablename__ = 'material'

  id = Column(INTEGER, primary_key=True)
  name = Column(Text, nullable=False)
  link = Column(Text, nullable=False)
  course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  def __init__(self, params):
    self.name = params["name"]
    self.link = params["link"]
    self.course_id = params["course_id"]


class Price(Base):
  __tablename__ = 'price'

  id = Column(INTEGER, primary_key=True)
  course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
  price = Column(DECIMAL(10, 0), nullable=False)
  is_active = Column(BIT(1))
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  def __init__(self, params):
    self.course_id = params["course_id"]
    self.price = params["price"]
    self.is_active = params["is_active"]


class DiscountPromotion(Base):
  __tablename__ = 'discount_promotion'

  id = Column(INTEGER, primary_key=True)
  course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
  discount = Column(Integer)
  begin_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
  end_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
  is_active = Column(BIT(1))
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  def __init__(self, params):
    self.course_id = params["course_id"]
    self.discount = params["discount"]
    self.begin_date = params["begin_date"]
    self.end_date = params["end_date"]
    self.is_active = params["is_active"]
