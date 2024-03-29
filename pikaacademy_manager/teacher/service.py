from logging import getLogger

from werkzeug.exceptions import InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash
from common.mail.send_mail import (sign_up_teacher, sign_up_teacher_successful)
from notification.dao import NotificationDAO
from common.constants import RoleTypeEnum, Notification
from .dao import TeacherDAO

logger = getLogger(__name__)


def change_password(body):
  try:
    logger.info(f'body: {body}')
    teacher = TeacherDAO.get_by_id(body["id"])
    res = {
      "message": '',
      "status": False
    }
    if teacher:
      teacher_info = TeacherDAO.get_by_email_pw(teacher.email)
      logger.info(f'teacher info: {teacher_info}')
      if not check_password_hash(teacher_info.hash_pwd, body["current_pw"]):
        res["message"] = 'Mật khẩu không đúng'
      else:
        if body["new_pw"] != body["confirm_pw"]:
          res["message"] = 'Mật khẩu của bạn và mật khẩu xác nhận không khớp.'
        else:
          TeacherDAO.update(body["id"], {"hash_pwd": generate_password_hash(body["new_pw"])})
          res["message"] = "Đổi mật khẩu thành công"
          res["status"] = True
    else:
      res["message"] = 'User not found'
    return res
  except Exception as e:
    raise InternalServerError(str(e.__cause__))


def sign_up(body):
  try:
    teacher = TeacherDAO.add(body)
    if teacher:
      sign_up_teacher(body["email"], teacher)
      content = f'{teacher.full_name} đã đăng ký trở thành giáo viên'
      notification_sql = []
      notification_admin = {
        "action_id": teacher.id,
        "content": content,
        "user_id": None,
        "role": RoleTypeEnum.Admin.value,
        "type": Notification.TeacherRegister.value,
      }
      notification_sql.append(notification_admin)
      if notification_sql:
        NotificationDAO.bulk_add(notification_sql)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))


def active_teacher(teacher_id):
  try:
    TeacherDAO.update(teacher_id, {'is_active': True})
    teacher = TeacherDAO.get_by_id(teacher_id)
    if teacher:
      sign_up_teacher_successful(teacher.email, teacher)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
