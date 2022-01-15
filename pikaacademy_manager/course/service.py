from logging import getLogger

from werkzeug.exceptions import InternalServerError

from .dao import CourseDAO, PriceDAO, DiscountPromotionDAO, MaterialDAO
from teacher.dao import TeacherDAO
from followed.dao import FollowerDAO
from user.dao import UserByCourse
from common.mail.send_mail import (add_course, uninstall, release_email)

logger = getLogger(__name__)


def add_courses(body):
  try:
    course_obj = {
      'name': body["name"],
      'description': body["description"],
      'about': body["about"],
      'url_image': body["url_image"],
      'url_intro_video': body["url_intro_video"],
      'result': body["result"],
      'level': body["level"],
      'interests_id': body["interests_id"],
      'category_id': body["category_id"],
      'teacher_id': body["teacher_id"],
      'created_by': body["created_by"],
      'updated_by': body["updated_by"]
    }
    course_id = CourseDAO.add(course_obj)
    if course_id:
      price_obj = {
        'course_id': course_id,
        'price': body["price"],
        'is_active': True
      }
      PriceDAO.add(price_obj)
      if body["discount"]:
        discount_promotion_obj = {
          'course_id': course_id,
          'discount': body["discount"],
          'begin_date': body["begin_date"],
          'end_date': body["end_date"],
          'is_active': True
        }
        DiscountPromotionDAO.add(discount_promotion_obj)
    material_arr = []
    for item in body["material"]:
      material_obj = {
        'name': item["name"],
        'link': item["link"],
        'course_id': course_id
      }
      material_arr.append(material_obj)
    if material_arr:
      MaterialDAO.bulk_add(material_arr)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))


def update_course(course_id, body):
  try:
    course_obj = {
      'name': body["name"],
      'description': body["description"],
      'about': body["about"],
      'url_image': body["url_image"],
      'url_intro_video': body["url_intro_video"],
      'result': body["result"],
      'level': body["level"],
      'interests_id': body["interests_id"],
      'category_id': body["category_id"],
      'teacher_id': body["teacher_id"],
      'created_by': body["created_by"],
      'updated_by': body["updated_by"]
    }
    CourseDAO.update(course_id, course_obj)
    price = PriceDAO.get_by_id(body["price_id"])
    if price.price != body["price"]:
      PriceDAO.inactive(body["price_id"])
      price_obj = {
        'course_id': course_id,
        'price': body["price"],
        'is_active': True
      }
      PriceDAO.add(price_obj)
    if body["discount_promotion_id"]:
      discount_promotion = DiscountPromotionDAO.get_by_id(body["discount_promotion_id"])
      if discount_promotion.discount != body["discount"] or discount_promotion.begin_date != body[
        "begin_date"] or discount_promotion.end_date != body["end_date"]:
        logger.info('update')
        DiscountPromotionDAO.inactive(body["discount_promotion_id"])
    if body["discount"]:
      discount_promotion_obj = {
        'course_id': course_id,
        'discount': body["discount"],
        'begin_date': body["begin_date"],
        'end_date': body["end_date"],
        'is_active': True
      }
      DiscountPromotionDAO.add(discount_promotion_obj)
    MaterialDAO.clear_by_course_id(course_id)
    material_arr = []
    for item in body["material"]:
      material_obj = {
        'name': item["name"],
        'link': item["link"],
        'course_id': course_id
      }
      material_arr.append(material_obj)
    if material_arr:
      MaterialDAO.bulk_add(material_arr)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))


def release(course_id):
  try:
    course = CourseDAO.get_by_id(course_id)
    release = course.release
    if course and course.is_active:
      if course.release:
        CourseDAO.update(course_id, {'release': False})
      else:
        release = True
        CourseDAO.update(course_id, {'release': True})
    teacher = TeacherDAO.get_by_id(course.teacher_id)
    if teacher:
      if release and course.release is None:
        followers = FollowerDAO.get_all_follower_by_teacher_id(teacher.id)
        if followers:
          for item in followers:
            obj = {
              "teacher_url_avatar": teacher.url_avatar,
              "teacher_name": teacher.full_name,
              "course_name": course.name,
              "course_url_intro_video": course.url_image
            }
            add_course(item.email, obj)
      if course.release is not None:
        users = UserByCourse.get_all_by_course_id(course_id)
        if users:
          for item in users:
            obj = {
              "name": f'{item.first_name} {item.last_name}',
              "course_name": course.name
            }
            if release:
              release_email(item.email, obj)
            else:
              uninstall(item.email, obj)
  except Exception as e:
    raise InternalServerError(str(e.__cause__))
