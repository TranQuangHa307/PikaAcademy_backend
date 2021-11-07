import os

from config import SENDGRID_API_KEY
from sendgrid import SendGridAPIClient
from logging import getLogger
from bs4 import BeautifulSoup
from flask import render_template
from jinja2 import Environment, FileSystemLoader
_location_ = os.path.dirname(os.path.realpath(__file__))
logger = getLogger(__name__)

def sign_up_successfully(email, user):
  message = {
    'personalizations': [
      {
        'to': [
          {
            'email': email
          }
        ],
        'dynamic_template_data': {
          'name': f'{user.first_name} {user.last_name}'
        }
      }
    ],
    'from': {
      'email': 'hoanganhtestkfe99@gmail.com'
    },
    "template_id": "d-35d4c9f6c8c8477aba7b711efdbcc1b8"
  }
  try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    logger.info(response.status_code)
    logger.info(response.body)
    logger.info(response.headers)
  except Exception as e:
    logger.info(str(e))


def successfully_transaction(email, transaction, transaction_courses):
  total_amount = transaction.total - ((transaction.total / 100) * transaction.discount)
  logger.info(f'full_name: {transaction.first_name} {transaction.last_name}')
  logger.info(f'code: {transaction.code}')
  logger.info(f'total: {transaction.total}')
  logger.info(f'discount: {transaction.discount}')
  logger.info(f'total_amount: {total_amount}')
  j2_env = Environment(loader=FileSystemLoader(_location_), trim_blocks=True)
  tm = j2_env.get_template("templates/successful_transaction.html")
  content_html = tm.render(transaction_courses=transaction_courses)
  # for item in transaction_courses:
  #   total = (item.original_price / 100) * item.discount
  #   transaction_str += f'<tr><td>{item.course_name}</td><td>{float(item.original_price)}</td><td>{item.discount}</td><td>{float(total)}</td></tr>'
  # transaction_str = BeautifulSoup(transaction_str).get_text()
  logger.info(f'transaction: {content_html}')
  message = {
    'personalizations': [
      {
        'to': [
          {
            'email': email
          }
        ],
        'dynamic_template_data': {
          'full_name': f'{transaction.first_name} {transaction.last_name}',
          'code': transaction.code,
          'total': float(transaction.total),
          'discount': transaction.discount,
          'total_amount': float(total_amount),
          'transactions': content_html
        }
      }
    ],
    'from': {
      'email': 'hoanganhtestkfe99@gmail.com'
    },
    "template_id": "d-09fffcbff4eb46ceb583ad370a9d93f0"
  }
  try:
    logger.info('send')
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    logger.info(response.status_code)
    logger.info(response.body)
    logger.info(response.headers)
  except Exception as e:
    logger.info(str(e))
