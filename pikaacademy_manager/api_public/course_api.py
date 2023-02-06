from logging import getLogger

from common.models import Pagination
from common.parameters import pagination_parameter
from common.res_base import paginate_result, parse
from course.dao import CourseDAO
from comment.dao import CommentDAO, ReplyCommentDAO
from flask import request
from flask_restplus import Namespace, Resource
from rating.dao import RatingDAO
from user.dao import UserByCourse, UserPurchaseCourseDAO
from .parameters import (pagination_parameter_course_list,
                         pagination_parameter_course_by_type,
                         parameter_teacher_courses,
                         user_parameter)

logger = getLogger(__name__)

api = Namespace('api/course', description='Public APIs For Course')


@api.route('')
class CourseListController(Resource):
    @api.doc()
    @api.expect(pagination_parameter_course_list, validate=True)
    def get(self):
        args = pagination_parameter_course_list.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(CourseDAO.get_list(paging))


@api.route('/<course_id>')
@api.response(404, 'Course not found.')
class CourseController(Resource):
    @api.doc()
    @api.expect(user_parameter, validate=True)
    def get(self, course_id):
        args = user_parameter.parse_args(request)
        user_id = args["user_id"]
        return parse(CourseDAO.get_by_id(course_id, user_id))


@api.route('/type')
class CourseListByTypeController(Resource):
    @api.doc()
    @api.expect(pagination_parameter_course_by_type, validate=True)
    def get(self):
        args = pagination_parameter_course_by_type.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(CourseDAO.get_list(paging, True))


@api.route('/teacher')
class TeacherCoursesController(Resource):
    @api.doc()
    @api.expect(parameter_teacher_courses, validate=True)
    def get(self):
        args = parameter_teacher_courses.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(CourseDAO.get_list(paging, True))


@api.route('/<course_id>/ratings')
class RatingCourseController(Resource):
    @api.doc()
    @api.expect(pagination_parameter, validate=True)
    def get(self, course_id):
        args = pagination_parameter.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(RatingDAO.get_by_course_id(paging, course_id))


@api.route('/<course_id>/comments')
class CommentCourseController(Resource):
    @api.doc()
    @api.expect(pagination_parameter, validate=True)
    def get(self, course_id):
        args = pagination_parameter.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(CommentDAO.get_list_by_course(paging, course_id))


@api.route('/comment/<comment_id>/reply')
class ReplyCommentCourseController(Resource):
    @api.doc()
    @api.expect(pagination_parameter, validate=True)
    def get(self, comment_id):
        args = pagination_parameter.parse_args(request)
        paging = Pagination.from_arguments(args)
        return paginate_result(ReplyCommentDAO.get_list_by_comment(paging, comment_id))
