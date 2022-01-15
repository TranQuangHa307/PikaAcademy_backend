from flask_restplus import reqparse

pagination_parameter = reqparse.RequestParser()
pagination_parameter.add_argument("page", type=int, location="args")
pagination_parameter.add_argument("limit", type=int, location="args")
pagination_parameter.add_argument("keyword", type=str, location="args")
pagination_parameter.add_argument("status", type=str, location="args")

