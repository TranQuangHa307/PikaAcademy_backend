from werkzeug.exceptions import Forbidden, HTTPException, Unauthorized


class PikaAcademyException(HTTPException):
    code = 400


class UserNotHasPermissionException(PikaAcademyException):
    code = Forbidden.code
    description = "User have no permission to implement this action"


class UserNotFoundException(PikaAcademyException):
    code = 400
    description = "The specified user name or password is incorrect."

class EmailExistxception(PikaAcademyException):
    code = 400
    description = "Your Email address exist"
