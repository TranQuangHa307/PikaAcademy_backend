from logging import getLogger

from libs.sql_action import db
from session.models import Session
from sqlalchemy import asc, and_
from werkzeug.exceptions import InternalServerError

from .models import Chapter

logger = getLogger(__name__)


class ChapterDAO(object):
  @staticmethod
  def get_by_course_id(course_id):
    try:
      res_query = db.session.query(
        Chapter.id,
        Chapter.name,
        Chapter.course_id,
        Session.id.label("session_id"),
        Session.name.label("session_name"),
        Session.url_video.label("session_url_video"),
        Session.time.label("session_time"),
        Session.created_at.label("session_created_at"),
        Session.updated_at.label("session_updated_at")
      ).outerjoin(Session,
                  and_(Session.chapter_id == Chapter.id,
                       Session.deleted_flag.isnot(True))) \
        .filter(Chapter.course_id == course_id,
                Chapter.deleted_flag.isnot(True)) \
        .order_by(asc(Chapter.created_at)).all()
      res = []
      for item in res_query:
        index = next((res.index(x) for x in res if x["id"] == item.id), None)
        if index:
          res[index]["sessions"].append({
            "id": item.session_id,
            "name": item.session_name,
            "chapter_id": item.id,
            "url_video": item.session_url_video,
            "time": item.session_time,
            "created_at": item.session_created_at,
            "updated_at": item.session_updated_at
          })
        else:
          obj = {
            "id": item.id,
            "name": item.name,
            "course_id": item.course_id,
            "sessions": [
              {
                "id": item.session_id,
                "name": item.session_name,
                "chapter_id": item.id,
                "url_video": item.session_url_video,
                "time": item.session_time,
                "created_at": item.session_created_at,
                "updated_at": item.session_updated_at
              }
            ]
          }
          res.append(obj)
      return res
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def add(params):
    try:
      chapter = Chapter(params)
      Chapter.create(chapter)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def update(chapter_id, data_dict):
    try:
      Chapter.update(chapter_id, data_dict)
    except Exception as e:
      raise InternalServerError(str(e.__cause__))

  @staticmethod
  def delete(chapter_id):
    try:
      Chapter.update(chapter_id, {"deleted_flag": True})
    except Exception as e:
      raise InternalServerError(str(e.__cause__))
