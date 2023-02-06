# coding: utf-8
from flask_restx import fields
from libs.sql_action import Base
from sqlalchemy import Column, DateTime, Text, text, ForeignKey
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR
from sqlalchemy.orm import relationship

session_fields = {
  "name": fields.String(required=True),
  "url_video": fields.String(required=True),
  "chapter_id": fields.Integer(required=True),
  "time": fields.Integer(required=True),
  "created_by": fields.String(required=True),
  "updated_by": fields.String(required=True),
  "exercise": fields.List(fields.Raw())
}


class Session(Base):
  __tablename__ = 'session'

  id = Column(INTEGER, primary_key=True)
  name = Column(Text, nullable=False)
  about = Column(Text, nullable=False)
  url_video = Column(Text, nullable=False)
  time = Column(INTEGER, nullable=False)
  chapter_id = Column(ForeignKey('chapter.id'), nullable=False, index=True)
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  created_by = Column(VARCHAR(256), nullable=False)
  updated_by = Column(VARCHAR(256), nullable=False)
  deleted_flag = Column(BIT(1))

  chapter = relationship('Chapter', backref="sessions")

  def __init__(self, params):
    self.name = params["name"]
    self.about = params["about"]
    self.url_video = params["url_video"]
    self.chapter_id = params["chapter_id"]
    self.time = params["time"]
    self.created_by = params["created_by"]
    self.updated_by = params["updated_by"]

class Exercise(Base):
  __tablename__ = 'exercise'

  id = Column(INTEGER, primary_key=True)
  name = Column(Text, nullable=False)
  link = Column(Text, nullable=False)
  session_id = Column(ForeignKey('session.id'), nullable=False, index=True)
  created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  deleted_flag = Column(BIT(1))

  def __init__(self, params):
    self.name = params["name"]
    self.link = params["link"]
    self.session_id = params["session_id"]