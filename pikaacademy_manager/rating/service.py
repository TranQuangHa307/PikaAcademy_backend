from user.dao import UserPurchaseCourseDAO
from werkzeug.exceptions import InternalServerError
from notification.dao import NotificationDAO
from common.constants import RoleTypeEnum, Notification
from user.dao import UserDAO
from course.dao import CourseDAO
from .dao import RatingDAO


def addRating(params):
    try:
        rating_obj = {
            "rating": params["rating"],
            "comment": params["comment"],
            "course_id": params["course_id"],
            "user_id": params["user_id"]
        }
        RatingDAO.add(rating_obj)
        UserPurchaseCourseDAO.update_is_rating(params["user_purchase_course_id"])
        user = UserDAO.get_by_id(params["user_id"])
        course = CourseDAO.get_by_id(params["course_id"])
        if user and course:
            user_name = f'{user.first_name} {user.last_name}'
            content = f'{user_name} đã đánh giá khoá học {course.name}'
            notification_sql = []
            notification_teacher = {
                "action_id": params["course_id"],
                "content": content,
                "user_id": course.teacher_id,
                "role": RoleTypeEnum.Teacher.value,
                "type": Notification.Rating.value,
            }
            notification_admin = {
                "action_id": params["course_id"],
                "content": content,
                "user_id": None,
                "role": RoleTypeEnum.Admin.value,
                "type": Notification.Rating.value,
            }
            notification_sql.append(notification_teacher)
            notification_sql.append(notification_admin)
            if notification_sql:
                NotificationDAO.bulk_add(notification_sql)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))
