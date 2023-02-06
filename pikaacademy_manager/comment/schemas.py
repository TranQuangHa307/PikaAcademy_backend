from flask_marshmallow import Marshmallow
from .models import Comment, ReplyComment

ma = Marshmallow()

class ReplyCommentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ReplyComment
        include_fk = True

    id = ma.auto_field()
    content = ma.auto_field()
    comment_id = ma.auto_field()
    user_id = ma.auto_field()
    user_name = ma.auto_field()
    role = ma.auto_field()
    created_at = ma.Function(lambda obj: obj["created_at"].timestamp() if obj["created_at"] else None)

class CommentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Comment

    id = ma.auto_field()
    content = ma.auto_field()
    course_id = ma.auto_field()
    user_id = ma.auto_field()
    user_name = ma.auto_field()
    role = ma.auto_field()
    created_at = ma.Function(lambda obj: obj["created_at"].timestamp() if obj["created_at"] else None)
