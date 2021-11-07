from libs.sql_action import db, safe_commit
from werkzeug.exceptions import InternalServerError
from sqlalchemy import desc, asc
from .models import Session


class SessionDAO(object):
  @staticmethod
  def get_by_chapter_id(chapter_id):
    try:
      res_query = db.session.query(
        Session.id,
        Session.name,
        Session.url_video,
        Session.chapter_id
      ).filter(Session.chapter_id == chapter_id, Session.deleted_flag.isnot(True)) \
        .order_by(asc(Session.created_at)).all()
      return res_query
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      session = Session(params)
      Session.create(session)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update(session_id, data_dict):
    try:
      Session.update(session_id, data_dict)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def delete(session_id):
    try:
      Session.update(session_id, {"deleted_flag": True})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
