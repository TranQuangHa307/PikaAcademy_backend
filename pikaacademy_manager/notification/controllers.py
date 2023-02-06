from logging import getLogger
from common.constants import RoleTypeEnum
from libs.auth import AuthenticatedResource
from common.res_base import parse, paginate_result, result_all
from flask import request
from flask_restplus import Namespace, reqparse, Resource
from .dao import NotificationDAO
from .models import notification_id_fields

logger = getLogger(__name__)
api = Namespace("notification", description='Notification related operations')

notification_id_model = api.model("Notification id model", notification_id_fields)


@api.route('/admin')
class AdminNotificationController(AuthenticatedResource):
    @api.doc()
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
    def get(self):
        return result_all(NotificationDAO.get_by_admin())

@api.route('/teacher/<teacher_id>')
class TeacherNotificationController(AuthenticatedResource):
    @api.doc()
    @AuthenticatedResource.roles_required([RoleTypeEnum.Teacher.value])
    def get(self, teacher_id):
        return result_all(NotificationDAO.get_by_teacher(teacher_id))

@api.route('/user/<user_id>')
class UserNotificationController(AuthenticatedResource):
    @api.doc()
    @AuthenticatedResource.roles_required([RoleTypeEnum.User.value])
    def get(self, user_id):
        return result_all(NotificationDAO.get_by_user(user_id))

@api.route('/seen')
class SeenNotificationController(AuthenticatedResource):
    @api.doc()
    @api.expect(notification_id_model, validate=True)
    @api.response(204, 'SeenNotification.')
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
    def put(self):
        NotificationDAO.is_seen(api.payload)
        return None, 204
