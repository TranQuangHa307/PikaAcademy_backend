from logging import getLogger

from common.models import Pagination
from common.res_base import paginate_result, result_all
from flask import request
from flask_restplus import Namespace, reqparse, Resource
from libs.auth import AuthenticatedResource
from category.dao import CategoryDAO

from .dao import InterestsDAO
from .models import interests_fields
from .service import (get_interests_by_id)

logger = getLogger(__name__)
api = Namespace("interests", description='Interests related operations')

interest_model = api.model("Interests", interests_fields)

pagination_parameter = reqparse.RequestParser()
pagination_parameter.add_argument("page", type=int, location="args")
pagination_parameter.add_argument("limit", type=int, location="args")
pagination_parameter.add_argument("keyword", type=str, location="args")


@api.route('')
class InterestsListController(AuthenticatedResource):
    @api.doc()
    @api.expect(pagination_parameter, validate=True)
    @AuthenticatedResource.roles_required(['admin'])
    def get(self):
        args = pagination_parameter.parse_args(request)
        paging = Pagination.from_arguments(args)
        return InterestsDAO.get_list(paging)

    @api.doc()
    @api.response(201, 'Interests successfully created.')
    @api.expect(interest_model, validate=True)
    @AuthenticatedResource.roles_required(['admin'])
    def post(self):
        InterestsDAO.create(api.payload)
        return None, 201

@api.route('/all')
class InterestsAllController(AuthenticatedResource):
    @api.doc()
    def get(self):
        return result_all(InterestsDAO.get_all())

@api.route('/<interests_id>')
@api.response(404, 'Interests not found.')
class InterestsController(AuthenticatedResource):
    @api.doc()
    def get(self, interests_id):
        return get_interests_by_id(interests_id)

    @api.doc()
    @api.expect(interest_model, validate=True)
    @api.response(204, 'Interests successfully updated.')
    @AuthenticatedResource.roles_required(['admin'])
    def put(self, interests_id):
        InterestsDAO.update(interests_id, api.payload)
        return None, 204

    @api.doc()
    @api.response(204, "Interests successfully deleted.")
    @AuthenticatedResource.roles_required(['admin'])
    def delete(self, interests_id):
        InterestsDAO.delete(interests_id)
        return None, 204

@api.route('/<interest_id>/category')
class CourseChapterController(Resource):
    @api.doc()
    def get(self, interest_id):
        return result_all(CategoryDAO.get_category_by_interests_id(interest_id))
