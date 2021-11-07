# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Enum, Integer, Text, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR
from libs.sql_action import Base
from flask_restx import fields

chapter_fields = {
    "name": fields.String(required=True),
    "course_id": fields.Integer(required=True),
    "created_by": fields.String(required=True),
    "updated_by": fields.String(required=True),
}
class Chapter(Base):
    __tablename__ = 'chapter'

    id = Column(INTEGER, primary_key=True)
    name = Column(Text, nullable=False)
    course_id = Column(INTEGER, nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    created_by = Column(VARCHAR(256), nullable=False)
    updated_by = Column(VARCHAR(256), nullable=False)
    deleted_flag = Column(BIT(1))

    def __init__(self, params):
        self.name = params["name"]
        self.course_id = params["course_id"]
        self.created_by = params["created_by"]
        self.updated_by = params["updated_by"]
