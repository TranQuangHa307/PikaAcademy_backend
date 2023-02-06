from logging import getLogger

from werkzeug.exceptions import InternalServerError

from .dao import CourseDAO, MaterialDAO
from teacher.dao import TeacherDAO
from followed.dao import FollowerDAO
from user.dao import UserByCourse
from common.mail.send_mail import (add_course, uninstall, release_email)
from notification.dao import NotificationDAO
from common.constants import RoleTypeEnum, Notification

logger = getLogger(__name__)


def add_courses(body):
    try:
        course_obj = {
            'name': body["name"],
            'description': body["description"],
            'about': body["about"],
            'url_image': body["url_image"],
            'url_intro_video': body["url_intro_video"],
            'is_active': body["is_active"],
            'release': body["release"],
            'result': body["result"],
            'level': body["level"],
            'interests_id': body["interests_id"],
            'category_id': body["category_id"],
            'teacher_id': body["teacher_id"],
            'created_by': body["created_by"],
            'updated_by': body["updated_by"]
        }
        course_id = CourseDAO.add(course_obj)
        material_arr = []
        for item in body["material"]:
            material_obj = {
                'name': item["name"],
                'link': item["link"],
                'course_id': course_id
            }
            material_arr.append(material_obj)
        if material_arr:
            MaterialDAO.bulk_add(material_arr)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))


def update_course(course_id, body):
    try:
        course_obj = {
            'name': body["name"],
            'description': body["description"],
            'about': body["about"],
            'url_image': body["url_image"],
            'url_intro_video': body["url_intro_video"],
            'result': body["result"],
            'level': body["level"],
            'interests_id': body["interests_id"],
            'category_id': body["category_id"],
            'teacher_id': body["teacher_id"],
            'created_by': body["created_by"],
            'updated_by': body["updated_by"]
        }
        CourseDAO.update(course_id, course_obj)
        MaterialDAO.clear_by_course_id(course_id)
        material_arr = []
        for item in body["material"]:
            material_obj = {
                'name': item["name"],
                'link': item["link"],
                'course_id': course_id
            }
            material_arr.append(material_obj)
        if material_arr:
            MaterialDAO.bulk_add(material_arr)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))


def active(course_id):
    course = CourseDAO.get_by_id(course_id)
    if course:
        CourseDAO.update(course_id, {'is_active': True})
        teacher = TeacherDAO.get_by_id(course.teacher_id)
        content = f'{teacher.full_name} đã đăng tải khóa học {course.name} đang chờ xác nhận!'
        notification_sql = []
        notification_admin = {
            "action_id": course.id,
            "content": content,
            "user_id": None,
            "role": RoleTypeEnum.Admin.value,
            "type": Notification.ActivityCourse.value,
        }
        notification_sql.append(notification_admin)
        if notification_sql:
            NotificationDAO.bulk_add(notification_sql)


def release(course_id):
    try:
        course = CourseDAO.get_by_id(course_id)
        release = course.release
        if course and course.is_active:
            teacher = TeacherDAO.get_by_id(course.teacher_id)
            followers = FollowerDAO.get_all_follower_by_teacher_id(teacher.id)
            content = f'Khóa học {course.name} đã được phát hành'
            notification_sql = []
            if course.release:
                CourseDAO.update(course_id, {'release': False})
            else:
                release = True
                CourseDAO.update(course_id, {'release': True})
                notification_teacher = {
                    "action_id": course.id,
                    "content": content,
                    "user_id": course.teacher_id,
                    "role": RoleTypeEnum.Teacher.value,
                    "type": Notification.ReleaseCourse.value,
                }
                notification_sql.append(notification_teacher)
                if followers:
                    for item in followers:
                        notification_user = {
                            "action_id": course.id,
                            "content": content,
                            "user_id": item.user_id,
                            "role": RoleTypeEnum.User.value,
                            "type": Notification.ReleaseCourse.value,
                        }
                        notification_sql.append(notification_user)

        if teacher:
            if release and course.release is None:
                if followers:
                    for item in followers:
                        obj = {
                            "teacher_url_avatar": teacher.url_avatar,
                            "teacher_name": teacher.full_name,
                            "course_name": course.name,
                            "course_url_intro_video": course.url_image
                        }
                        add_course(item.email, obj)
            if course.release is not None:
                users = UserByCourse.get_all_by_course_id(course_id)
                if users:
                    for item in users:
                        obj = {
                            "name": f'{item.first_name} {item.last_name}',
                            "course_name": course.name
                        }
                        if release:
                            release_email(item.email, obj)
                        else:
                            uninstall(item.email, obj)
        if notification_sql:
            NotificationDAO.bulk_add(notification_sql)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))
