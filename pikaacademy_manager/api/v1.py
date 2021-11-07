from flask import Blueprint
from flask_restplus import Api

from admin.controllers import api as admin_api
from course.controllers import api as course_api
from interests.controllers import api as interests_api
from category.controllers import api as category_api
from chapter.controllers import api as chapter_api
from session.controllers import api as session_api
from teacher.controllers import api as teacher_api
from user.controllers import api as user_api
from cart.controllers import api as cart_api
from transaction.controllers import api as transaction_api
from .common import api as common_api
from api_public.teacher_api import api as teacher_api_public
from api_public.course_api import api as course_api_public
from api_public.interests_api import api as interests_api_public
from api_public.category_api import api as category_api_public
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api_bp = Blueprint("api", __name__)

api = Api(
    title='Edumall API',
    version='1.0',
    description='A simple demo API',
    security=['apikey'],
    authorizations=authorizations
)

api.add_namespace(course_api)
api.add_namespace(admin_api)
api.add_namespace(interests_api)
api.add_namespace(category_api)
api.add_namespace(common_api)
api.add_namespace(chapter_api)
api.add_namespace(session_api)
api.add_namespace(teacher_api)
api.add_namespace(user_api)
api.add_namespace(cart_api)
api.add_namespace(transaction_api)
api.add_namespace(teacher_api_public)
api.add_namespace(course_api_public)
api.add_namespace(interests_api_public)
api.add_namespace(category_api_public)


