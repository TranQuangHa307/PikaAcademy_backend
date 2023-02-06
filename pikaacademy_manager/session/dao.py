from libs.sql_action import db, safe_commit
from werkzeug.exceptions import InternalServerError
from sqlalchemy import desc, asc
from .models import Session, Exercise


class SessionDAO(object):
    @staticmethod
    def get_by_chapter_id(chapter_id):
        try:
            res_query = db.session.query(
                Session.id,
                Session.name,
                Session.url_video,
                Session.description,
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
            return session.id
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


class ExerciseDAO(object):
    @staticmethod
    def get_list_by_session_id(session_id):
        try:
            res_query = db.session.query(
                Exercise.id,
                Exercise.name,
                Exercise.session_id,
                Exercise.link
            ).filter(Exercise.session_id == session_id,
                     Exercise.deleted_flag.isnot(True))
            res_query = res_query.group_by(Exercise.id).order_by(Exercise.created_at).all()
            return res_query
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def bulk_add(exercise_arr):
        try:
            exercise_sql = []
            for item in exercise_arr:
                exercise = Exercise(item)
                exercise_sql.append(exercise)
            if exercise_sql:
                db.session.bulk_save_objects(exercise_sql)
                safe_commit()
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def clear_by_session_id(session_id):
        try:
            db.session.query(Exercise).filter(Exercise.session_id == session_id,
                                              Exercise.deleted_flag.isnot(True)).update(
                dict(deleted_flag=1))
            safe_commit()
        except Exception as e:
            raise InternalServerError(str(e.__cause__))
