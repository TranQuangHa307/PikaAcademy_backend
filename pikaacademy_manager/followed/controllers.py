from logging import getLogger

from common.constants import RoleTypeEnum
from common.parameters import pagination_parameter
from common.res_base import paginate_result
from flask import request
from flask_restplus import Namespace
from libs.auth import AuthenticatedResource

from .dao import FollowerDAO
from .models import followed_fields
from .service import (follow_teacher)

logger = getLogger(__name__)
api = Namespace("followed", description='Followed related operations')

followed_model = api.model("Followed", followed_fields)


@api.route('/')
class FollowedController(AuthenticatedResource):
  @api.doc()
  @api.expect(followed_model, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value, RoleTypeEnum.User.value])
  def post(self):
    is_active = follow_teacher(api.payload)
    return is_active, 201


@api.route('/teacher/<teacher_id>/follower')
class FollowerController(AuthenticatedResource):
  @api.doc()
  @api.expect(pagination_parameter, validate=True)
  @AuthenticatedResource.roles_required([RoleTypeEnum.Admin.value, RoleTypeEnum.Teacher.value])
  def get(self, teacher_id):
    args = pagination_parameter.parse_args(request)
    return paginate_result(FollowerDAO.get_follower_by_teacher_id(args, teacher_id))
