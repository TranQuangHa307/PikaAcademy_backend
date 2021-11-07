from libs.sql_action import db

from .models import AdminAccount


class AdminAccountDAO(object):
    @staticmethod
    def get_account_by_id(account_id):
        res_query = db.session.query(
            AdminAccount.id,
            AdminAccount.user_name,
            AdminAccount.email,
            AdminAccount.role
        ).filter(AdminAccount.id == account_id, AdminAccount.deleted_flag.isnot(True)).first()
        return res_query