from logging import getLogger
from user.models import User
from teacher.models import Teacher
from admin.models import AdminAccount
from course.models import Course
from .models import Comment, ReplyComment
from common.models import Pagination
from libs.sql_action import db, safe_commit
from teacher.models import Teacher
from sqlalchemy import desc, and_, or_, func
from werkzeug.exceptions import InternalServerError

logger = getLogger(__name__)


class CommentDAO(object):
    @staticmethod
    def get_list_by_course(args: Pagination, course_id, is_delete=False):
        try:
            res_query = db.session.query(
                Comment.id,
                Comment.content,
                Comment.course_id,
                Comment.created_at,
                Comment.user_id,
                Comment.role,
                User.first_name.label('user_first_name'),
                User.last_name.label('user_last_name'),
                User.url_avatar.label('user_url_avatar'),
                Teacher.full_name.label('teacher_full_name'),
                Teacher.url_avatar.label('teacher_url_avatar'),
                AdminAccount.user_name.label('admin_user_name'),
                func.count(ReplyComment.id).label("count_reply_comment")
            ).outerjoin(User, User.id == Comment.user_id)\
                .outerjoin(Teacher, Teacher.id == Comment.teacher_id)\
                .outerjoin(AdminAccount, AdminAccount.id == Comment.admin_id)\
                .outerjoin(ReplyComment, and_(ReplyComment.comment_id == Comment.id,
                                           ReplyComment.deleted_flag.isnot(True)))\
                .where(Comment.course_id == course_id)
            if is_delete:
                res_query = res_query.where(Comment.deleted_flag.isnot(True))
            res_query = res_query.group_by(Comment.id).order_by(desc(Comment.created_at)) \
                .paginate(args.page, args.limit)
            return res_query
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def get_by_id(comment_id):
        try:
            res_query = db.session.query(
                Comment.id,
                Comment.content,
                Comment.course_id,
                Comment.created_at,
                Comment.user_id,
                Comment.teacher_id,
                Comment.admin_id,
                Comment.role,
                Course.name.label('course_name'),
                Course.teacher_id.label('course_teacher_id'),
                User.first_name.label('user_first_name'),
                User.last_name.label('user_last_name'),
                User.url_avatar.label('user_url_avatar'),
                Teacher.full_name.label('teacher_full_name'),
                Teacher.url_avatar.label('teacher_url_avatar'),
                AdminAccount.user_name.label('admin_user_name')
            ).join(Course, Course.id == Comment.course_id)\
                .outerjoin(User, User.id == Comment.user_id)\
                .outerjoin(Teacher, Teacher.id == Comment.teacher_id)\
                .outerjoin(AdminAccount, AdminAccount.id == Comment.admin_id)\
                .where(Comment.id == comment_id).first()
            return res_query
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def add(params):
        try:
            logger.info(f'comment1: {params}')
            comment = Comment(params)
            logger.info(f'comment2: {params}')
            Comment.create(comment)
            return comment.id
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def update(comment_id, data_dict):
        try:
            Comment.update(comment_id, data_dict)
        except Exception:
            raise InternalServerError()

    @staticmethod
    def delete(comment_id):
        try:
            Course.update(comment_id, {"deleted_flag": True})
        except Exception:
            raise InternalServerError()


class ReplyCommentDAO(object):

    @staticmethod
    def get_by_id(reply_comment_id):
        try:
            res_query = db.session.query(
                ReplyComment.id,
                ReplyComment.content,
                ReplyComment.comment_id,
                ReplyComment.user_id,
                ReplyComment.teacher_id,
                ReplyComment.admin_id,
                ReplyComment.role,
                ReplyComment.created_at,
                User.first_name.label('user_first_name'),
                User.last_name.label('user_last_name'),
                User.url_avatar.label('user_url_avatar'),
                Teacher.full_name.label('teacher_full_name'),
                Teacher.url_avatar.label('teacher_url_avatar'),
                AdminAccount.user_name.label('admin_user_name')
            ).outerjoin(User, User.id == ReplyComment.user_id) \
                .outerjoin(Teacher, Teacher.id == ReplyComment.teacher_id) \
                .outerjoin(AdminAccount, AdminAccount.id == ReplyComment.admin_id) \
                .where(ReplyComment.id == reply_comment_id).first()
            return res_query
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def get_list_by_comment(args: Pagination, comment_id, is_delete=False):
        try:
            res_query = db.session.query(
                ReplyComment.id,
                ReplyComment.content,
                ReplyComment.user_id,
                ReplyComment.role,
                ReplyComment.created_at,
                User.first_name.label('user_first_name'),
                User.last_name.label('user_last_name'),
                User.url_avatar.label('user_url_avatar'),
                Teacher.full_name.label('teacher_full_name'),
                Teacher.url_avatar.label('teacher_url_avatar'),
                AdminAccount.user_name.label('admin_user_name')
            ).outerjoin(User, User.id == ReplyComment.user_id) \
                .outerjoin(Teacher, Teacher.id == ReplyComment.teacher_id) \
                .outerjoin(AdminAccount, AdminAccount.id == ReplyComment.admin_id) \
                .where(ReplyComment.comment_id == comment_id)
            if is_delete:
                res_query = res_query.where(ReplyComment.deleted_flag.isnot(True))
            res_query = res_query.order_by(desc(ReplyComment.created_at)) \
                .paginate(args.page, args.limit)
            return res_query
        except Exception as e:
            raise InternalServerError(str(e.__cause__))

    @staticmethod
    def add(params):
        try:
            reply_comment = ReplyComment(params)
            ReplyComment.create(reply_comment)
            return reply_comment.id
        except Exception as e:
            raise InternalServerError(str(e.__cause__))
