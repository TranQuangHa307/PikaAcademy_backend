# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, String, Text, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR
from libs.sql_action import Base
from flask_restx import fields

teacher_fields = {
    "full_name": fields.String(required=True),
    "email": fields.String(required=True),
    "url_avatar": fields.String(required=True),
    "date_of_birth": fields.DateTime(required=True),
    "gender": fields.String(),
    "phone_number": fields.String(required=True),
    "about": fields.String(required=True)
}


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(INTEGER, primary_key=True)
    full_name = Column(VARCHAR(256), nullable=False)
    email = Column(VARCHAR(256), nullable=False)
    url_avatar = Column(Text, nullable=False)
    date_of_birth = Column(DateTime)
    gender = Column(Enum('not_specific', 'male', 'female'), nullable=False, server_default=text("'not_specific'"))
    phone_number = Column(String(11))
    about = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_flag = Column(BIT(1))

    def __init__(self, params):
        self.full_name = params["full_name"]
        self.email = params["email"]
        self.url_avatar = params["url_avatar"]
        self.date_of_birth = params["date_of_birth"]
        self.gender = params["gender"]
        self.phone_number = params["phone_number"]
        self.about = params["about"]
