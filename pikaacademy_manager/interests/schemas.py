from flask_marshmallow import Marshmallow
from category.schemas import CategorySchema

from .models import Interests

ma = Marshmallow()

class InterestsSchema(ma.SQLAlchemySchema):
  class Meta:
    model = Interests

  id = ma.auto_field()
  name = ma.auto_field()
  description = ma.auto_field()
  url_image = ma.auto_field()
  categories = ma.Nested(CategorySchema, many=True)
