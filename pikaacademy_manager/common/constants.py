from enum import Enum

class RoleTypeEnum(Enum):
  User = 'user'
  Admin = 'admin'

class TransactionStatusEnum(Enum):
  Initial = 'initial'
  Pending = 'pending'
  Success = 'success'
  Canceled = 'canceled'