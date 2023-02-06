from logging import getLogger

from common.mail.send_mail import (sign_up_successfully)
from course.dao import CourseDAO
from teacher.dao import TeacherDAO
from werkzeug.exceptions import InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash
from notification.dao import NotificationDAO
from common.constants import RoleTypeEnum, Notification
from .dao import UserLikeCourseDAO, UserDAO, UserPurchaseCourseDAO

logger = getLogger(__name__)
def user_purchase_course(params):
    try:
        user_purchase_course_obj = {
            "user_id": params["user_id"],
            "course_id": params["course_id"]
        }
        UserPurchaseCourseDAO.add(user_purchase_course_obj)
        course = CourseDAO.get_by_id(params["course_id"])
        user = UserDAO.get_by_id(params["user_id"])
        number_purchases = course.purchases + 1
        CourseDAO.update(course.id, {"purchases": number_purchases})
        if user and course:
            user_name = f'{user.first_name} {user.last_name}'
            content = f'{user_name} đã đăng ký khoá học {course.name}'
            notification_sql = []
            notification_teacher = {
                "action_id": params["course_id"],
                "content": content,
                "user_id": course.teacher_id,
                "role": RoleTypeEnum.Teacher.value,
                "type": Notification.UerPurchaseCourse.value,
            }
            notification_admin = {
                "action_id": params["course_id"],
                "content": content,
                "user_id": None,
                "role": RoleTypeEnum.Admin.value,
                "type": Notification.UerPurchaseCourse.value,
            }
            notification_sql.append(notification_teacher)
            notification_sql.append(notification_admin)
            if notification_sql:
                NotificationDAO.bulk_add(notification_sql)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))

def user_like_course(params):
    try:
        course = CourseDAO.get_by_id(params["course_id"])
        teacher = TeacherDAO.get_by_id(course.teacher_id)
        res = None
        if course:
            user_like_course_db = UserLikeCourseDAO.get_by_id(params["course_id"], params["user_id"])
            if user_like_course_db:
                UserLikeCourseDAO.delete(user_like_course_db.id)
                number_likes = course.likes - 1
                number_likes_teacher = teacher.likes - 1
            else:
                _id = UserLikeCourseDAO.add(params)
                number_likes = course.likes + 1
                number_likes_teacher = teacher.likes + 1
                res = _id
                user = UserDAO.get_by_id(params["user_id"])
                if user and course:
                    user_name = f'{user.first_name} {user.last_name}'
                    content = f'{user_name} đã thích khoá học {course.name}'
                    notification_sql = []
                    notification_teacher = {
                        "action_id": params["course_id"],
                        "content": content,
                        "user_id": course.teacher_id,
                        "role": RoleTypeEnum.Teacher.value,
                        "type": Notification.Like.value,
                    }
                    notification_admin = {
                        "action_id": params["course_id"],
                        "content": content,
                        "user_id": None,
                        "role": RoleTypeEnum.Admin.value,
                        "type": Notification.Like.value,
                    }
                    notification_sql.append(notification_teacher)
                    notification_sql.append(notification_admin)
                    if notification_sql:
                        NotificationDAO.bulk_add(notification_sql)
            CourseDAO.update(course.id, {"likes": number_likes})
            TeacherDAO.update(teacher.id, {"likes": number_likes_teacher})
        return res
    except Exception as e:
        raise InternalServerError(str(e.__cause__))


def sign_up(body):
    try:
        user = UserDAO.add(body)
        if user:
            sign_up_successfully(body["email"], user)
            user_name = f'{user.first_name} {user.last_name}'
            content = f'{user_name} đã đăng ký tài khoản user'
            # notification_sql = []
            # notification_admin = {
            #     "action_id": user.id,
            #     "content": content,
            #     "user_id": None,
            #     "role": RoleTypeEnum.Admin.value,
            #     "type": Notification.UserRegister.value,
            # }
            # notification_sql.append(notification_admin)
            # if notification_sql:
            #     NotificationDAO.bulk_add(notification_sql)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))


def change_password(body):
    try:
        logger.info(f'body: {body}')
        user = UserDAO.get_by_id(body["id"])
        res = {
            "message": '',
            "status": False
        }
        if user:
            logger.info(f'user: {user}')
            user_info = UserDAO.get_by_email(user.email)
            if not check_password_hash(user_info.hash_pwd, body["current_pw"]):
                res["message"] = 'Mật khẩu không đúng'
            else:
                if body["new_pw"] != body["confirm_pw"]:
                    res["message"] = 'Mật khẩu của bạn và mật khẩu xác nhận không khớp.'
                else:
                    UserDAO.update(body["id"], {"hash_pwd": generate_password_hash(body["new_pw"])})
                    res["message"] = "Đổi mật khẩu thành công"
                    res["status"] = True
        else:
            res["message"] = 'User not found'
        return res
    except Exception as e:
        raise InternalServerError(str(e.__cause__))
