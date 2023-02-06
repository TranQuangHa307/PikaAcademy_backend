# coding: utf-8
from common.models import NullableString, NullableInteger
from flask_restx import fields
from libs.sql_action import Base
from sqlalchemy import Column, DECIMAL, DateTime, Enum, Integer, Text, text, ForeignKey
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR

comment_fields = {
    "content": fields.String(required=True),
    "course_id": fields.Integer(required=True),
    "user_id": fields.Integer(),
    "teacher_id": fields.Integer(),
    "admin_id": fields.Integer(),
    "role": fields.String(required=True)
}

reply_comment_fields = {
    "content": fields.String(required=True),
    "comment_id": fields.Integer(required=True),
    "user_id": fields.Integer(),
    "teacher_id": fields.Integer(),
    "admin_id": fields.Integer(),
    "role": fields.String(required=True)
}


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(INTEGER, primary_key=True)
    content = Column(Text, nullable=False)
    course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
    user_id = Column(INTEGER, nullable=True)
    teacher_id = Column(INTEGER, nullable=True)
    admin_id = Column(INTEGER, nullable=True)
    role = Column(Enum('admin', 'teacher', 'user'), nullable=False, server_default=text("'not_specific'"))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_flag = Column(BIT(1))

    def __init__(self, params):
        self.content = params["content"]
        self.course_id = params["course_id"]
        self.user_id = params["user_id"]
        self.teacher_id = params["teacher_id"]
        self.admin_id = params["admin_id"]
        self.role = params["role"]


class ReplyComment(Base):
    __tablename__ = 'reply_comment'
    id = Column(INTEGER, primary_key=True)
    content = Column(Text, nullable=False)
    comment_id = Column(ForeignKey('comment.id'), nullable=False, index=True)
    user_id = Column(INTEGER, nullable=True)
    teacher_id = Column(INTEGER, nullable=True)
    admin_id = Column(INTEGER, nullable=True)
    role = Column(Enum('admin', 'teacher', 'user'), nullable=False, server_default=text("'not_specific'"))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_flag = Column(BIT(1))

    def __init__(self, params):
        self.content = params["content"]
        self.comment_id = params["comment_id"]
        self.user_id = params["user_id"]
        self.teacher_id = params["teacher_id"]
        self.admin_id = params["admin_id"]
        self.role = params["role"]
