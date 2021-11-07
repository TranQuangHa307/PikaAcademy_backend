from functools import wraps

from flask_jwt_extended import (jwt_required, get_jwt_claims, verify_jwt_in_request)
from flask_restx import Resource

from exceptions import UserNotHasPermissionException


class AuthenticatedResource(Resource):
    method_decorators = [jwt_required]

    @classmethod
    def roles_required(cls, roles):
        def roles_required_deco(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                verify_jwt_in_request()
                role = get_jwt_claims()["role"]
                if role not in roles:
                    raise UserNotHasPermissionException
                else:
                    return fn(*args, **kwargs)

            return wrapper

        return roles_required_deco
