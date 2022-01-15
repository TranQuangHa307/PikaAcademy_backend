from flask_restplus import reqparse

pagination_parameter = reqparse.RequestParser()
pagination_parameter.add_argument("page", type=int, location="args")
pagination_parameter.add_argument("limit", type=int, location="args")
pagination_parameter.add_argument("keyword", type=str, location="args")

change_password_parameters = reqparse.RequestParser()
change_password_parameters.add_argument("id", type=int, required=True, location="form", default=0,
                                        help="Id")
change_password_parameters.add_argument("current_pw", type=str, required=True, location="form", default="",
                                        help="Current password")
change_password_parameters.add_argument("new_pw", type=str, required=True, location="form", default="",
                                        help="New password")
change_password_parameters.add_argument("confirm_pw", type=str, required=True, location="form", default="",
                                        help="Confirm password")
