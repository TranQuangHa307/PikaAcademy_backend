# coding: utf-8
from flask_restx import fields
from libs.sql_action import Base
from sqlalchemy import Column, DateTime, Text, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR

interests_fields = {
    "name": fields.String(required=True),
    "description": fields.String(required=True),
    "url_image": fields.String(),
    "created_by": fields.String(required=True),
    "updated_by": fields.String(required=True)
}


class Interests(Base):
    __tablename__ = 'interests'

    id = Column(INTEGER, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    url_image = Column(Text)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    created_by = Column(VARCHAR(256), nullable=False)
    updated_by = Column(VARCHAR(256), nullable=False)
    deleted_flag = Column(BIT(1))

    def __init__(self, params):
        self.name = params["name"]
        self.description = params["description"]
        self.url_image = params["url_image"]
        self.created_by = params["created_by"]
        self.updated_by = params["updated_by"]
