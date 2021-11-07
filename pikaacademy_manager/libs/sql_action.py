# -*- coding: utf-8 -*-

"""sql_action.py
Database factory for all modules to use
"""
from logging import getLogger

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
logger = getLogger(__name__)


def safe_commit():
  """
  Commit change and rollback if the commit error
  :return:
  """
  try:
    db.session.commit()
  except Exception as e:
    logger.info(e)
    db.session.rollback()
    raise


class Base(db.Model):
  __abstract__ = True

  session = db.session

  @classmethod
  def find_all(cls, condition):
    return cls.session.query(cls).filter_by(**condition).all()

  @classmethod
  def find_by_id(cls, _id):
    return cls.session.query(cls).get(_id)

  @classmethod
  def find_one(cls, condition):
    return cls.session.query(cls).filter_by(**condition).first()

  def create(self):
    self.session.add(self)
    safe_commit()

  @classmethod
  def update(cls, _id, update_dict):
    obj = cls.session.query(cls).filter_by(id=_id).update(update_dict)
    try:
      cls.session.commit()
      return obj
    except:  # noqa
      cls.session.rollback()
      raise

  def delete(self):
    self.session.delete(self)
    safe_commit()

  def merge(self):
    self.session.merge(self)
    safe_commit()
