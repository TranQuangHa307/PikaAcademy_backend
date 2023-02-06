from logging import getLogger

from teacher.dao import TeacherDAO
from werkzeug.exceptions import InternalServerError
from notification.dao import NotificationDAO
from common.constants import RoleTypeEnum, Notification
from user.dao import UserDAO
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
    if follow["is_active"]:
      TeacherDAO.update(teacher.id, {"followed": (teacher.followed + 1)})
      user = UserDAO.get_by_id(params["user_id"])
      if user:
        user_name = f'{user.first_name} {user.last_name}'
        notification_sql = []
        notification_teacher = {
          "action_id": params["teacher_id"],
          "content": f'{user_name} đã bắt đầu theo dõi bạn',
          "user_id": params["teacher_id"],
          "role": RoleTypeEnum.Teacher.value,
          "type": Notification.Follow.value,
        }
        notification_admin = {
          "action_id": params["teacher_id"],
          "content": f'{user_name} đã bắt đầu theo dõi {teacher.full_name}',
          "user_id": None,
          "role": RoleTypeEnum.Admin.value,
          "type": Notification.Follow.value,
        }
        notification_sql.append(notification_teacher)
        notification_sql.append(notification_admin)
        if notification_sql:
          NotificationDAO.bulk_add(notification_sql)
    else:
      if teacher.followed > 0:
        TeacherDAO.update(teacher.id, {"followed": (teacher.followed - 1)})
    return follow["is_active"]
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
