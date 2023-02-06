from logging import getLogger
from flask import request
from flask_restplus import Namespace, reqparse
from libs.auth import AuthenticatedResource
from common.parameters import pagination_parameter
from common.constants import RoleTypeEnum
from .dao import CommentDAO, ReplyCommentDAO
from .models import comment_fields, reply_comment_fields
from.service import (add_comment, add_reply_comment)
from common.models import Pagination
from common.res_base import parse, paginate_result, result_all

logger = getLogger(__name__)
api = Namespace("comment", description='Comments related operations')

comment_model = api.model("Comment", comment_fields)
reply_comment_model = api.model("ReplyComment", reply_comment_fields)


@api.route('/course/<course_id>')
@api.response(404, 'Course not found.')
class CommentListByCourseController(AuthenticatedResource):
    @api.doc()
    @api.expect(pagination_parameter, validate=True)
    @AuthenticatedResource.roles_required(
        [RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
    def get(self, course_id):
        args = pagination_parameter.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(CommentDAO.get_list_by_course(paging, course_id))

    @api.doc()
    @api.expect(comment_model, validate=True)
    @AuthenticatedResource.roles_required(
        [RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
    def post(self, course_id):
        add_comment(api.payload)
        return None, 201


@api.route('/<comment_id>')
@api.response(404, 'Comment not found.')
class CommentController(AuthenticatedResource):
    @api.doc()
    @api.expect(comment_model, validate=True)
    @api.response(204, 'Comment successfully updated.')
    @AuthenticatedResource.roles_required(
        [RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
    def put(self, comment_id):
        CommentDAO.update(comment_id, api.payload)
        return None, 204

    @api.doc()
    @api.response(204, "Comment successfully deleted.")
    @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
    def delete(self, comment_id):
        CommentDAO.delete(comment_id)
        return None, 204


@api.route('/<comment_id>/reply')
@api.response(404, 'Comment not found.')
class ReplyCommentController(AuthenticatedResource):
    @api.doc()
    @api.expect(pagination_parameter, validate=True)
    @AuthenticatedResource.roles_required(
        [RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
    def get(self, comment_id):
        args = pagination_parameter.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(ReplyCommentDAO.get_list_by_comment(paging, comment_id))

    @api.doc()
    @api.expect(reply_comment_model, validate=True)
    @AuthenticatedResource.roles_required(
        [RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
    def post(self, comment_id):
        add_reply_comment(api.payload)
        return None, 201
