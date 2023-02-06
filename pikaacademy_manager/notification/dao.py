from logging import getLogger
from common.constants import RoleTypeEnum
from libs.sql_action import db, safe_commit
from sqlalchemy import desc, and_, or_, func
from werkzeug.exceptions import InternalServerError

from .models import Notification

logger = getLogger(__name__)


class NotificationDAO(object):

    @staticmethod
    def get_by_admin():
        try:
            res_query = db.session.query(
                Notification.id,
                Notification.content,
                Notification.action_id,
                Notification.user_id,
                Notification.role,
                Notification.type,
                Notification.created_at,
                Notification.is_seen
            ).where(Notification.deleted_flag.isnot(True),
                    Notification.role==RoleTypeEnum.Admin.value)
            res_query = res_query.group_by(Notification.id) \
                .order_by(desc(Notification.created_at)).all()
            return res_query
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def get_by_teacher(teacher_id):
        try:
            res_query = db.session.query(
                Notification.id,
                Notification.content,
                Notification.action_id,
                Notification.user_id,
                Notification.role,
                Notification.type,
                Notification.created_at,
                Notification.is_seen
            ).where(Notification.deleted_flag.isnot(True),
                    Notification.user_id == teacher_id,
                    Notification.role == RoleTypeEnum.Teacher.value)
            res_query = res_query.group_by(Notification.id) \
                .order_by(desc(Notification.created_at)).all()
            return res_query
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def get_by_user(user_id):
        try:
            res_query = db.session.query(
                Notification.id,
                Notification.content,
                Notification.action_id,
                Notification.user_id,
                Notification.role,
                Notification.type,
                Notification.created_at,
                Notification.is_seen
            ).where(Notification.deleted_flag.isnot(True),
                    Notification.user_id == user_id,
                    Notification.role == RoleTypeEnum.User.value)
            res_query = res_query.group_by(Notification.id) \
                .order_by(desc(Notification.created_at)).all()
            return res_query
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def add(params):
        try:
            notification = Notification(params)
            Notification.create(notification)
            return notification.id
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def bulk_add(notification_arr):
        try:
            notification_sql = []
            for item in notification_arr:
                notification = Notification(item)
                notification_sql.append(notification)
            if notification_sql:
                db.session.bulk_save_objects(notification_sql)
                safe_commit()
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def is_seen(ids):
        try:
            logger.info(f'{ids["ids"]}')
            db.session.query(Notification).filter(Notification.id.in_(ids["ids"])).update({'is_seen': True})
            safe_commit()
        except Exception as e:
            raise InternalServerError(str(e.__cause__))
