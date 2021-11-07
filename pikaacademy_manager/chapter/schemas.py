from flask_marshmallow import Marshmallow
from session.models import Session

from .models import Chapter

ma = Marshmallow()

class SessionSchema(ma.SQLAlchemySchema):
  class Meta:
    model = Session
    include_fk = True

  id = ma.auto_field()
  name = ma.auto_field()
  url_video = ma.auto_field()
  time = ma.auto_field()
  created_at = ma.Function(lambda obj: obj["created_at"].timestamp() if obj["created_at"] else None)
  updated_at = ma.Function(lambda obj: obj["updated_at"].timestamp() if obj["updated_at"] else None)

class ChapterSchema(ma.SQLAlchemySchema):
  class Meta:
    model = Chapter

  id = ma.auto_field()
  name = ma.auto_field()
  sessions = ma.Nested(SessionSchema, many=True)
