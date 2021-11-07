from logging import getLogger
from flask_restplus import Namespace
from libs.auth import AuthenticatedResource
from .dao import SessionDAO
from .models import session_fields

logger = getLogger(__name__)
api = Namespace("session", description='Sessions related operations')

session_model = api.model("Chapter", session_fields)


@api.route('')
class SessionListController(AuthenticatedResource):
    @api.doc()
    @api.expect(session_model, validate=True)
    def post(self):
        SessionDAO.add(api.payload)
        return None, 201

@api.route('/<session_id>')
@api.response(404, 'Course not found.')
class ChapterController(AuthenticatedResource):
    @api.doc()
    @api.expect(session_model, validate=True)
    @api.response(204, 'Session successfully updated.')
    @AuthenticatedResource.roles_required(['admin'])
    def put(self, session_id):
        SessionDAO.update(session_id, api.payload)
        return None, 204

    @api.doc()
    @api.response(204, "Session successfully deleted.")
    @AuthenticatedResource.roles_required(['admin'])
    def delete(self, session_id):
        SessionDAO.delete(session_id)
        return None, 204


