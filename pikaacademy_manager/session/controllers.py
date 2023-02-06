from logging import getLogger
from flask_restplus import Namespace
from libs.auth import AuthenticatedResource
from .dao import SessionDAO, ExerciseDAO
from .models import session_fields
from common.constants import RoleTypeEnum
from common.res_base import parse, paginate_result, result_all
from .service import (add_session, update_session)

logger = getLogger(__name__)
api = Namespace("session", description='Sessions related operations')

session_model = api.model("Chapter", session_fields)


@api.route('')
class SessionListController(AuthenticatedResource):
    @api.doc()
    @api.expect(session_model, validate=True)
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
    def post(self):
        add_session(api.payload)
        return None, 201

@api.route('/<session_id>')
@api.response(404, 'Course not found.')
class ChapterController(AuthenticatedResource):
    @api.doc()
    @api.expect(session_model, validate=True)
    @api.response(204, 'Session successfully updated.')
    @AuthenticatedResource.roles_required(['admin', 'teacher'])
    def put(self, session_id):
        update_session(session_id, api.payload)
        return None, 204

    @api.doc()
    @api.response(204, "Session successfully deleted.")
    @AuthenticatedResource.roles_required(['admin', 'teacher'])
    def delete(self, session_id):
        SessionDAO.delete(session_id)
        return None, 204

@api.route('/<session_id>/exericse')
@api.response(404, 'Session not found.')
class ExerciseListController(AuthenticatedResource):
    @api.doc()
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
    def get(self, session_id):
        return result_all(ExerciseDAO.get_list_by_session_id(session_id))
