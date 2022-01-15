from logging import getLogger

from teacher.dao import TeacherDAO
from werkzeug.exceptions import InternalServerError

from .dao import FollowerDAO

logger = getLogger(__name__)


def follow_teacher(params):
  try:
    logger.info(f'{params}')
    follow = FollowerDAO.get_by_user_teacher_id(params["user_id"], params["teacher_id"])
    logger.info(f'follow: {follow}')
    if follow:
      follow = {
        "id": follow[0],
        "user_id": follow[1],
        "teacher_id": follow[2],
        "is_active": not follow[3]
      }
      FollowerDAO.update(follow["id"], follow)
    else:
      follow = {
        "user_id": params["user_id"],
        "teacher_id": params["teacher_id"],
        "is_active": 1
      }
      FollowerDAO.add(follow)
    teacher = TeacherDAO.get_by_id(params["teacher_id"])
    logger.info(f'teacher: {teacher.id}')
    logger.info(f'teacher: {teacher.followed}')
    if follow["is_active"]:
      TeacherDAO.update(teacher.id, {"followed": (teacher.followed + 1)})
    else:
      if teacher.followed > 0:
        TeacherDAO.update(teacher.id, {"followed": (teacher.followed - 1)})
    return follow["is_active"]
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
