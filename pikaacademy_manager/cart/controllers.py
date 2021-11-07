from logging import getLogger
from common.res_base import parse, paginate_result, result_all
from flask import request
from libs.auth import AuthenticatedResource
from common.constants import RoleTypeEnum
from .models import cart_fields, cart_course_fields
from flask_restplus import Namespace, reqparse, Resource
from .dao import CartDAO, CartCourseDAO
from .service import (add_cart_course)

logger = getLogger(__name__)
api = Namespace("cart", description="Cart related operations")
cart_model = api.model("Cart", cart_fields)
cart_course_model = api.model("Cart Course", cart_course_fields)

pagination_parameter = reqparse.RequestParser()
pagination_parameter.add_argument("page", type=int, location="args")
pagination_parameter.add_argument("limit", type=int, location="args")


@api.route('')
class CartListController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.User.value])
  @api.expect(cart_model, validate=True)
  @api.response(204, 'Cart successfully created.')
  def post(self):
    CartDAO.add(api.payload)
    return None, 201


@api.route('/<cart_id>/course')
@api.response(404, 'Cart not found')
class CartCourseListController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.User.value])
  def get(self, cart_id):
    return result_all(CartCourseDAO.get_list_by_cart_id(cart_id))

@api.route('/course')
class CartCourseController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.User.value])
  @api.expect(cart_course_model, validate=True)
  @api.response(204, 'Cart successfully created.')
  def post(self):
    add_cart_course(api.payload)
    return None, 201

@api.route('/course/<cart_course_id>')
@api.response(404, 'Cart not found')
class CartCourseIdController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.User.value])
  @api.response(204, 'Cart course successfully deleted.')
  def delete(self, cart_course_id):
    CartCourseDAO.delete(cart_course_id)
    return None, 201