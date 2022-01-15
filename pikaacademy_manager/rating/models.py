# coding: utf-8
from flask_restx import fields
from libs.sql_action import Base
from sqlalchemy import Column, DateTime, Text, text, ForeignKey
from sqlalchemy.dialects.mysql import BIT, INTEGER
from sqlalchemy.orm import relationship

rating_fields = {
  "rating": fields.Integer(required=True),
  "comment": fields.String(required=True),
  "course_id": fields.Integer(required=True),
  "user_id": fields.Integer(required=True),
}


class Rating(Base):
  __tablename__ = 'rating'

  id = Column(INTEGER, primary_key=True)
  rating = Column(INTEGER, nullable=False)
  comment = Column(Text, nullable=False)
  course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
  user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  course = relationship('Course')
  user = relationship('User')

  def __init__(self, params):
    self.rating = params["rating"]
    self.comment = params["comment"]
    self.course_id = params["course_id"]
    self.user_id = params["user_id"]
