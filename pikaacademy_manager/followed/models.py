# coding: utf-8
from flask_restx import fields
from libs.sql_action import Base
from sqlalchemy import Column, DateTime, text, ForeignKey
from sqlalchemy.dialects.mysql import BIT, INTEGER
from sqlalchemy.orm import relationship

followed_fields = {
  "teacher_id": fields.Integer(required=True),
  "user_id": fields.Integer(required=True),
  "is_active": fields.Boolean()
}


class Followed(Base):
  __tablename__ = 'followed'

  id = Column(INTEGER, primary_key=True)
  teacher_id = Column(ForeignKey('teacher.id'), nullable=False, index=True)
  user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
  is_active = Column(BIT(1))
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  teacher = relationship('Teacher')
  user = relationship('User')

  def __init__(self, params):
    self.teacher_id = params["teacher_id"]
    self.user_id = params["user_id"]
    self.is_active = params["is_active"]
