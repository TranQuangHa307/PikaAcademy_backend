# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, VARCHAR, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AdminAccount(Base):
    __tablename__ = 'admin_account'

    id = Column(INTEGER, primary_key=True)
    user_name = Column(VARCHAR(256), nullable=False)
    email = Column(VARCHAR(256), nullable=False)
    password = Column(LONGTEXT, nullable=False)
    role = Column(Enum('admin', 'member'), nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    created_by = Column(VARCHAR(256), nullable=False)
    updated_by = Column(VARCHAR(256), nullable=False)
    deleted_flag = Column(BIT(1))
