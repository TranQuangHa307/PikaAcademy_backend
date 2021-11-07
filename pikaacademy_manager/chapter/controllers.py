from logging import getLogger
from flask import request
from common.res_base import result_all, parse
from flask_restplus import Namespace, reqparse, Resource
from libs.auth import AuthenticatedResource
from common.models import Pagination
from session.dao import SessionDAO
from .dao import ChapterDAO
from .models import chapter_fields
from common.constants import RoleTypeEnum
logger = getLogger(__name__)
api = Namespace("chapter", description='Chapters related operations')

chapter_model = api.model("Chapter", chapter_fields)


@api.route('')
class ChapterListController(AuthenticatedResource):
    @api.doc()
    @api.expect(chapter_model, validate=True)
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
    def post(self):
        ChapterDAO.add(api.payload)
        return None, 201

@api.route('/<chapter_id>')
@api.response(404, 'Course not found.')
class ChapterController(AuthenticatedResource):
    @api.doc()
    @api.expect(chapter_model, validate=True)
    @api.response(204, 'Course successfully updated.')
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
    def put(self, chapter_id):
        ChapterDAO.update(chapter_id, api.payload)
        return None, 204

    @api.doc()
    @api.response(204, "Course successfully deleted.")
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
    def delete(self, chapter_id):
        ChapterDAO.delete(chapter_id)
        return None, 204

@api.route('/<chapter_id>/session')
class ChapterSessionController(Resource):
    @api.doc()
    def get(self, chapter_id):
        return result_all(SessionDAO.get_by_chapter_id(chapter_id))

