from user.dao import UserPurchaseCourseDAO
from werkzeug.exceptions import InternalServerError

from .dao import RatingDAO


def addRating(params):
  try:
    rating_obj = {
      "rating": params["rating"],
      "comment": params["comment"],
      "course_id": params["course_id"],
      "user_id": params["user_id"]
    }
    RatingDAO.add(rating_obj)
    UserPurchaseCourseDAO.update_is_rating(params["user_purchase_course_id"])
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
