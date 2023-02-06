from flask_restplus import reqparse

pagination_parameter_course_list = reqparse.RequestParser()
pagination_parameter_course_list.add_argument("page", type=int, location="args")
pagination_parameter_course_list.add_argument("limit", type=int, location="args")
pagination_parameter_course_list.add_argument("keyword", type=str, location="args")
pagination_parameter_course_list.add_argument("user_id", type=int, location="args")
pagination_parameter_course_list.add_argument("interests", action='split', location="args")
pagination_parameter_course_list.add_argument("categories", action='split', location="args")
pagination_parameter_course_list.add_argument("levels", action='split', location="args")

pagination_parameter_course_by_type = reqparse.RequestParser()
pagination_parameter_course_by_type.add_argument("page", type=int, location="args")
pagination_parameter_course_by_type.add_argument("limit", type=int, location="args")
pagination_parameter_course_by_type.add_argument("user_id", type=int, location="args")
pagination_parameter_course_by_type.add_argument("type", type=str, location="args")

parameter_teacher_courses = reqparse.RequestParser()
parameter_teacher_courses.add_argument("page", type=int, location="args")
parameter_teacher_courses.add_argument("limit", type=int, location="args")
parameter_teacher_courses.add_argument("teacher_id", type=int, location="args")
parameter_teacher_courses.add_argument("user_id", type=int, location="args")

user_parameter = reqparse.RequestParser()
user_parameter.add_argument("user_id", type=int, location="args")