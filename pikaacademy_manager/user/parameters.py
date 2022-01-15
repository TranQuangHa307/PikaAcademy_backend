from flask_restplus import reqparse

login_parameters = reqparse.RequestParser()
login_parameters.add_argument("email", type=str, required=True, location="form", default="", help="User name")
login_parameters.add_argument("password", type=str, required=True, location="form", default="", help="User password")

sign_up_parameters = reqparse.RequestParser()
sign_up_parameters.add_argument("email", type=str, required=True, location="form", default="", help="User name")

pagination_parameter_transactions_user = reqparse.RequestParser()
pagination_parameter_transactions_user.add_argument("page", type=int, location="args")
pagination_parameter_transactions_user.add_argument("limit", type=int, location="args")
pagination_parameter_transactions_user.add_argument("status", action='split', location="args")

change_password_parameters = reqparse.RequestParser()
change_password_parameters.add_argument("id", type=int, required=True, location="form", default=0,
                                        help="Id")
change_password_parameters.add_argument("current_pw", type=str, required=True, location="form", default="",
                                        help="Current password")
change_password_parameters.add_argument("new_pw", type=str, required=True, location="form", default="",
                                        help="New password")
change_password_parameters.add_argument("confirm_pw", type=str, required=True, location="form", default="",
                                        help="Confirm password")

login_google_parameters = reqparse.RequestParser()
login_google_parameters.add_argument(
  "googleToken", type=str, required=True, location="form", default=""
)
login_google_parameters.add_argument(
  "userPictureUrl", type=str, location="form", default=None
)
