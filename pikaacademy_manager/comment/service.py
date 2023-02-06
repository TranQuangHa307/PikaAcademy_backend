from logging import getLogger
from .dao import CommentDAO, ReplyCommentDAO
from notification.dao import NotificationDAO
from common.constants import RoleTypeEnum, Notification
from werkzeug.exceptions import InternalServerError

logger = getLogger(__name__)

def add_comment(body):
    try:
        comment_id = CommentDAO.add(body)
        comment = CommentDAO.get_by_id(comment_id)
        if comment:
            user_name = get_user_name(comment)
            content = f'{user_name} đã bình luận khoá học {comment.course_name}'
            notification_sql = []
            if comment.role != RoleTypeEnum.Teacher.value:
                notification_teacher = {
                    "action_id": comment.course_id,
                    "content": content,
                    "user_id": comment.course_teacher_id,
                    "role": RoleTypeEnum.Teacher.value,
                    "type": Notification.Comment.value,
                }
                notification_sql.append(notification_teacher)
            if comment.role != RoleTypeEnum.Admin.value:
                notification_admin = {
                    "action_id": comment.course_id,
                    "content": content,
                    "user_id": comment.admin_id,
                    "role": RoleTypeEnum.Admin.value,
                    "type": Notification.Comment.value,
                }
                notification_sql.append(notification_admin)
            if notification_sql:
                NotificationDAO.bulk_add(notification_sql)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))

def get_user_name(comment):
    user_name = ""
    if comment.role == RoleTypeEnum.User.value:
        user_name = f'{comment.user_first_name} {comment.user_last_name}'
    if comment.role == RoleTypeEnum.Teacher.value:
        user_name = comment.teacher_full_name
    if comment.role == RoleTypeEnum.Admin.value:
        user_name = comment.admin_user_name
    return  user_name

def add_reply_comment(body):
    try:
        reply_comment_id = ReplyCommentDAO.add(body)
        reply_comment = ReplyCommentDAO.get_by_id(reply_comment_id)
        if reply_comment:
            comment = CommentDAO.get_by_id(reply_comment.comment_id)
            if comment:
                user_name = get_user_name(reply_comment)
                content = f'{user_name} đã phản hồi một bình luận của khoá học {comment.course_name}',
                notification_sql = []
                if reply_comment.role != RoleTypeEnum.Admin.value:
                    notification_admin = {
                        "action_id": comment.course_id,
                        "content": content,
                        "user_id": comment.admin_id,
                        "role": RoleTypeEnum.Admin.value,
                        "type": Notification.ReplyComment.value,
                    }
                    notification_sql.append(notification_admin)
                if reply_comment.role != RoleTypeEnum.Teacher.value:
                    notification_teacher = {
                        "action_id": comment.course_id,
                        "content": content,
                        "user_id": comment.course_teacher_id,
                        "role": RoleTypeEnum.Teacher.value,
                        "type": Notification.ReplyComment.value,
                    }
                    notification_sql.append(notification_teacher)
                if reply_comment.role == RoleTypeEnum.User.value and comment.role == RoleTypeEnum.User.value:
                    if comment.user_id != reply_comment.user_id:
                        notification_user = {
                            "action_id": comment.course_id,
                            "content": content,
                            "user_id": comment.user_id,
                            "role": RoleTypeEnum.User.value,
                            "type": Notification.ReplyComment.value,
                        }
                        notification_sql.append(notification_user)
                if reply_comment.role != RoleTypeEnum.User.value and comment.role == RoleTypeEnum.User.value:
                    notification_user = {
                        "action_id": comment.course_id,
                        "content": content,
                        "user_id": comment.user_id,
                        "role": RoleTypeEnum.User.value,
                        "type": Notification.ReplyComment.value,
                    }
                    notification_sql.append(notification_user)

                if notification_sql:
                    logger.info(f'Arr: {notification_sql}')
                    NotificationDAO.bulk_add(notification_sql)
    except Exception as e:
        raise InternalServerError(str(e.__cause__))