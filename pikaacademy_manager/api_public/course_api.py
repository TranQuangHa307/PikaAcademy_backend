from logging import getLogger

from common.models import Pagination
from common.res_base import paginate_result, result_all, parse
from course.dao import CourseDAO
from transaction.dao import TransactionDAO, TransactionCourseDAO
from flask import request, jsonify
from flask_restplus import Namespace, Resource
from common.mail.send_mail import (successfully_transaction)
import paypalrestsdk
from .parameters import (pagination_parameter_course_list,
                         pagination_parameter_course_by_type,
                         parameter_teacher_courses,
                         user_parameter)

logger = getLogger(__name__)

api = Namespace('api/course', description='Public APIs For Course')

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "Aa0ieqkQYd1EKBwVY-8Ly0FmNf9ahbf4LAfaeKd-jfx_mSWHear7Q7qlUXDBCrynXkUM3zLwXM4KQwkB",
  "client_secret": "EDG9ChHZcoh7Y-PmmDknchNVw1EkxFY1Cq-2E0Z3p2LONshbBsDjKuifftZDSngURl5BNczhrOb-h47F" })

@api.route('/payment')
class TransactionController(Resource):
  @api.doc()
  def get(self):
    payment = paypalrestsdk.Payment({
      "intent": "sale",
      "payer": {
        "payment_method": "paypal"},
      "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
      "transactions": [{
        "item_list": {
          "items": [{
            "name": "item",
            "sku": "item",
            "price": "5.00",
            "currency": "USD",
            "quantity": 1}]},
        "amount": {
          "total": "5.00",
          "currency": "USD"},
        "description": "This is the payment transaction description."}]})

    if payment.create():
      print("Payment created successfully")
    else:
      print(payment.error)
    return jsonify({'paymentId': payment.id})

@api.route('')
class CourseListController(Resource):
  @api.doc()
  @api.expect(pagination_parameter_course_list, validate=True)
  def get(self):
    args = pagination_parameter_course_list.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(CourseDAO.get_list(paging))

@api.route('/<course_id>')
@api.response(404, 'Course not found.')
class CourseController(Resource):
  @api.doc()
  @api.expect(user_parameter, validate=True)
  def get(self, course_id):
    args = user_parameter.parse_args(request)
    user_id = args["user_id"]
    return parse(CourseDAO.get_by_id(course_id, user_id))


@api.route('/type')
class CourseListByTypeController(Resource):
  @api.doc()
  @api.expect(pagination_parameter_course_by_type, validate=True)
  def get(self):
    args = pagination_parameter_course_by_type.parse_args(request)
    paging = Pagination.from_arguments(args)
    email = 'hoanganhkfe99@gmail.com'
    transaction = TransactionDAO.get_by_id(19)
    logger.info(f'transaction: {transaction}')
    transaction_courses = TransactionCourseDAO.get_list_by_transaction(transaction_id=transaction.id)
    successfully_transaction(email, transaction, transaction_courses)
    return paginate_result(CourseDAO.get_list(paging))


@api.route('/teacher')
class TeacherCoursesController(Resource):
  @api.doc()
  @api.expect(parameter_teacher_courses, validate=True)
  def get(self):
    args = parameter_teacher_courses.parse_args(request)
    paging = Pagination.from_arguments(args)
    return paginate_result(CourseDAO.get_list(paging))
