from logging import getLogger


from common.models import Pagination
from common.res_base import parse, result_all, paginate_result
from flask import request
from flask_restplus import Namespace, reqparse, Resource
from libs.auth import AuthenticatedResource
from common.parameters import pagination_parameter
from common.constants import RoleTypeEnum
from .dao import TeacherDAO
from .models import teacher_fields

logger = getLogger(__name__)
api = Namespace("teacher", description='Teachers related operations')

teacher_model = api.model("Teacher", teacher_fields)


@api.route('/all')
class TeacherAllController(AuthenticatedResource):
    @api.doc()
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
    def get(self):
        return result_all(TeacherDAO.get_all())

@api.route('')
class TeacherListController(AuthenticatedResource):
    @api.doc()
    @api.expect(pagination_parameter, validate=True)
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
    def get(self):
        args = pagination_parameter.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(TeacherDAO.get_list(paging))

    @api.doc()
    @api.expect(teacher_model, validate=True)
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
    def post(self):
        TeacherDAO.add(api.payload)
        return None, 201



@api.route('/<teacher_id>')
@api.response(404, 'Teacher not found.')
class CourseController(Resource):
    @api.doc()
    def get(self, teacher_id):
        return parse(TeacherDAO.get_by_id(teacher_id))

    @api.doc()
    @api.expect(teacher_model, validate=True)
    @api.response(204, 'Teacher successfully updated.')
    @AuthenticatedResource.roles_required(['admin'])
    def put(self, teacher_id):
        TeacherDAO.update(teacher_id, api.payload)
        return None, 204

    @api.doc()
    @api.response(204, "Teacher successfully deleted.")
    @AuthenticatedResource.roles_required(['admin'])
    def delete(self, teacher_id):
        TeacherDAO.delete(teacher_id)
        return None, 204
