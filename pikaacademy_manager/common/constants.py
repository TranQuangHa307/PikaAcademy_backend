from enum import Enum

class RoleTypeEnum(Enum):
  User = 'user'
  Admin = 'admin'
  Teacher = 'teacher'

class TransactionStatusEnum(Enum):
  Initial = 'initial'
  Pending = 'pending'
  Success = 'success'
  Canceled = 'canceled'

class Notification(Enum):
  UserRegister = 1
  TeacherRegister = 2
  ActivityCourse = 3
  ReleaseCourse = 4
  Comment = 5
  ReplyComment = 6
  Rating = 7
  Like = 8
  UerPurchaseCourse = 9
  Follow = 10
