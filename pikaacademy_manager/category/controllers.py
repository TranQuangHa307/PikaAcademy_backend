from common.models import Pagination
from flask import request
from flask_restplus import Namespace, reqparse
from libs.auth import AuthenticatedResource
from common.res_base import parse
from .models import category_fields
from .dao import CategoryDAO
from common.constants import RoleTypeEnum
api = Namespace("category", description="Category related operations")

category_model = api.model("Category", category_fields)

pagination_parameter = reqparse.RequestParser()
pagination_parameter.add_argument("page", type=int, location="args")
pagination_parameter.add_argument("limit", type=int, location="args")
pagination_parameter.add_argument("keyword", type=str, location="args")

@api.route('')
class CategoryListController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required(['admin'])
  def get(self):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return CategoryDAO.get_list(paging)

  @api.doc()
  @api.response(201, 'Category successfully created.')
  @api.expect(category_model, validate=True)
  def post(self):
    # add_category(api.payload)
    CategoryDAO.add(api.payload)
    return None, 201

@api.route('/all')
class CategoryAllController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self):
    return CategoryDAO.get_all()

@api.route('/<category_id>')
@api.response(404, 'Category not found')
class CategoryController(AuthenticatedResource):
  @api.doc()
  def get(self, category_id):
    return parse(CategoryDAO.get_by_id(category_id))


  @api.doc()
  @api.expect(category_model, validate=True)
  @api.response(204, 'Category successfully updated.')
  @AuthenticatedResource.roles_required(['admin'])
  def put(self, category_id):
    CategoryDAO.update(category_id, api.payload)
    return None, 204

  @api.doc()
  @api.response(204, 'Category successfully deleted.')
  @AuthenticatedResource.roles_required(['admin'])
  def delete(self, category_id):
    CategoryDAO.delete(category_id)
    return None, 204