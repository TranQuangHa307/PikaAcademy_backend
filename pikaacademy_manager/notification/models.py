# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, String, Text, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR
from libs.sql_action import Base
from flask_restx import fields

notification_id_fields = {
    "ids": fields.List(fields.Integer)
}

class Notification(Base):
    __tablename__ = 'notification'

    id = Column(INTEGER, primary_key=True)
    content = Column(Text, nullable=False)
    action_id = Column(INTEGER, nullable=True)
    user_id = Column(INTEGER, nullable=True)
    role = Column(Enum('admin', 'teacher', 'user'), nullable=True)
    type = Column(INTEGER, nullable=True)
    is_seen = Column(BIT(1))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_flag = Column(BIT(1))

    def __init__(self, params):
        self.content =  params["content"]
        self.action_id = params["action_id"]
        self.user_id = params["user_id"]
        self.role = params["role"]
        self.type = params["type"]
