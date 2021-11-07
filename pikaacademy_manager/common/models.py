from flask_restx import fields

DEFAULT_SORT_FIELD = "created_at"
DEFAULT_SORT_ORDER = "desc"

class NullableString(fields.String):
  __schema_type__ = ["string", "null"]
  __schema_example__ = "nullable string"


class NullableInteger(fields.Integer):
  __schema_type__ = ["integer", "null"]
  __schema_example__ = "nullable integer"

# Common Classes
class Pagination:
  def __init__(
      self,
      page,
      limit,
      user_id,
      teacher_id,
      keyword,
      interests,
      categories,
      levels,
      prices,
      type,
      status
  ):
    self.page = page
    self.limit = limit
    self.user_id = user_id
    self.teacher_id = teacher_id
    self.keyword = keyword
    self.interests = interests
    self.categories = categories
    self.levels = levels
    self.prices = prices
    self.type = type
    self.status = status

  @classmethod
  def from_arguments(cls, args):
    page = args.page if 'page' in args and args.page else 1
    limit = args.limit if 'limit' in args and args.limit else 100
    user_id = args.user_id if 'user_id' in args and args.user_id else 0
    teacher_id = args.teacher_id if 'teacher_id' in args and args.teacher_id else 0
    keyword = args.keyword if 'keyword' in args and args.keyword else ""
    interests = args.interests if 'interests' in args and args.interests else []
    categories = args.categories if 'categories' in args and args.categories else []
    levels = args.levels if 'levels' in args and args.levels else []
    prices = args.prices if 'prices' in args and args.prices else []
    type = args.type if 'type' in args and args.type else ""
    status = args.status if 'status' in args and args.status else ""
    return cls(page, limit, user_id, teacher_id, keyword, interests, categories, levels, prices, type, status)
