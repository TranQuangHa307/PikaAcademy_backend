from flask_marshmallow import Marshmallow

from .models import Category

ma = Marshmallow()

class CategorySchema(ma.SQLAlchemySchema):
  class Meta:
    model = Category

  id = ma.auto_field()
  name = ma.auto_field()
  url_image = ma.auto_field()
