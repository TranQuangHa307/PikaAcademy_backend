# coding: utf-8
from flask_restx import fields
from libs.sql_action import Base
from sqlalchemy import Column, DateTime, Text, text, ForeignKey
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR
# from sqlalchemy.orm import relationship
# from interests.models import Interests

category_fields = {
  "name": fields.String(required=True),
  "url_image": fields.String(),
  "interests_id": fields.List(fields.Integer),
  "created_by": fields.String(required=True),
  "updated_by": fields.String(required=True)
}


class Category(Base):
  __tablename__ = 'category'

  id = Column(INTEGER, primary_key=True)
  name = Column(Text, nullable=False)
  url_image = Column(Text, nullable=False)
  interests_id = Column(ForeignKey('interests.id'), nullable=False, index=True)
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  created_by = Column(VARCHAR(256), nullable=False)
  updated_by = Column(VARCHAR(256), nullable=False)
  deleted_flag = Column(BIT(1))

  def __init__(self, params):
    self.name = params["name"]
    self.url_image = params["url_image"]
    self.interests_id = params["interests_id"]
    self.created_by = params["created_by"]
    self.updated_by = params["updated_by"]

