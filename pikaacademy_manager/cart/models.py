# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Text, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR
from sqlalchemy.orm import relationship
from libs.sql_action import Base
from flask_restx import fields

cart_fields = {
    "user_id": fields.Integer(required=True),
}

cart_course_fields = {
    "cart_id": fields.Integer(required=True),
    "course_id": fields.Integer(required=True),
}


class Cart(Base):
    __tablename__ = 'cart'

    id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_flag = Column(BIT(1))

    user = relationship('User')

    def __init__(self, params):
        self.user_id = params["user_id"]

class CartCourse(Base):
    __tablename__ = 'cart_course'

    id = Column(INTEGER, primary_key=True)
    cart_id = Column(ForeignKey('cart.id'), nullable=False, index=True)
    course_id = Column(ForeignKey('course.id'), nullable=False, index=True)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_flag = Column(BIT(1))

    cart = relationship('Cart')
    course = relationship('Course')

    def __init__(self, params):
        self.cart_id = params["cart_id"]
        self.course_id = params["course_id"]
