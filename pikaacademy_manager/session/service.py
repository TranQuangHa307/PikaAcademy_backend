from logging import getLogger
from .dao import SessionDAO, ExerciseDAO
from werkzeug.exceptions import InternalServerError

def add_session(body):
    try:
        session_obj = {
            'name': body["name"],
            'url_video': body["url_video"],
            'chapter_id': body["chapter_id"],
            'time': body["time"],
            'about': body["about"],
            'created_by': body["created_by"],
            'updated_by': body["updated_by"]
        }
        session_id = SessionDAO.add(session_obj)
        exercise_arr = []
        for item in body["exercise"]:
            exercise_obj = {
                "name": item["name"],
                "link": item["link"],
                "session_id": session_id
            }
            exercise_arr.append(exercise_obj)
        if exercise_arr:
            ExerciseDAO.bulk_add(exercise_arr)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))

def update_session(session_id, body):
    try:
        session_obj = {
            'name': body["name"],
            'url_video': body["url_video"],
            'about': body["about"],
            'time': body["time"],
            'created_by': body["created_by"],
            'updated_by': body["updated_by"],
        }
        SessionDAO.update(session_id, session_obj)
        ExerciseDAO.clear_by_session_id(session_id)
        exercise_arr = []
        for item in body["exercise"]:
            exercise_obj = {
                "name": item["name"],
                "link": item["link"],
                "session_id": session_id
            }
            exercise_arr.append(exercise_obj)
        if exercise_arr:
            ExerciseDAO.bulk_add(exercise_arr)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))
