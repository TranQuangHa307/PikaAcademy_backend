from logging import getLogger

from common.models import Pagination
from .parameters import pagination_parameter
from common.res_base import parse, result_all, paginate_result
from flask import request
from flask_restplus import Namespace
from libs.auth import AuthenticatedResource
from libs.constants import RoleTypeEnum

from .dao import TransactionDAO, TransactionCourseDAO
from .models import transaction_fields, transaction_change_fields
from .service import (transaction, update_transaction_status)

logger = getLogger(__name__)

api = Namespace("transaction", description="Transaction related operations")
transaction_model = api.model("Transaction", transaction_fields)
transaction_change_model = api.model("Transaction change", transaction_change_fields)


@api.route('')
class TransactionListController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def get(self):
    args = pagination_parameter.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(TransactionDAO.get_list(paging))

  @api.doc()
  @api.expect(transaction_model, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value, RoleTypeEnum.Admin.value])
  @api.response(204, 'Transaction successfully created.')
  def post(self):
    transaction_id = transaction(api.payload)
    return transaction_id, 201

@api.route('/status/<status>')
class TransactionListByStatusController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value])
  def get(self, status):
    return result_all(TransactionDAO.get_list_by_status(status))


@api.route('/<transaction_id>')
@api.response(404, 'Transaction not found')
class TransactionController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value, RoleTypeEnum.Admin.value])
  def get(self, transaction_id):
    return parse(TransactionDAO.get_by_id(transaction_id))

  @api.doc()
  @api.expect(transaction_change_model, validate=True)
  @api.response(204, 'Transaction successfully updated.')
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value, RoleTypeEnum.Admin.value])
  def put(self, transaction_id):
    update_transaction_status(transaction_id, api.payload)
    return None, 204


@api.route('/<transaction_id>/courses')
@api.response(404, 'Transaction not found')
class TransactionCourseListController(AuthenticatedResource):
  @api.doc()
  @AuthenticatedResource.roles_required([RoleTypeEnum.User.value, RoleTypeEnum.Admin.value])
  def get(self, transaction_id):
    return result_all(TransactionCourseDAO.get_list_by_transaction(transaction_id))
