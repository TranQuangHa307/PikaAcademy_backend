from flask_restplus import reqparse

login_parameters = reqparse.RequestParser()
login_parameters.add_argument("email", type=str, required=True, location="form", default="", help="Email")
login_parameters.add_argument("password", type=str, required=True, location="form", default="", help="Password")

sign_up_parameters = reqparse.RequestParser()
sign_up_parameters.add_argument("email", type=str, required=True, location="form", default="", help="Email")
