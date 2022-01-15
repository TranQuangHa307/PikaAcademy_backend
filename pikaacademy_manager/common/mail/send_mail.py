import os

from config import SENDGRID_API_KEY, port, smtp_server, sender_email, password
from sendgrid import SendGridAPIClient
from logging import getLogger
from bs4 import BeautifulSoup
from flask import render_template
from jinja2 import Environment, FileSystemLoader
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

_location_ = os.path.dirname(os.path.realpath(__file__))
logger = getLogger(__name__)

receiver_email = "hoanganhkfe99@gmail.com"  # Enter receiver address
j2_env = Environment(loader=FileSystemLoader(_location_), trim_blocks=True)


def set_header_email(receiver_email, subject):
  message = MIMEMultipart("alternative")
  message["Subject"] = subject
  message["From"] = "PikaAcademy"
  message["To"] = receiver_email
  return message


def sign_up_successfully(email, user):
  try:
    receiver_email = email
    context = ssl.create_default_context()
    message = set_header_email(receiver_email, 'Thank you for your registration!')
    tm = j2_env.get_template("templates/signup.html")
    content_html = tm.render(name=f'{user.first_name} {user.last_name}')
    message.attach(MIMEText(content_html, "html"))
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
  except Exception as e:
    logger.info(f'error: {e}')


def sign_up_teacher(email, teacher):
  try:
    receiver_email = email
    context = ssl.create_default_context()
    message = set_header_email(receiver_email, 'Thank you for your registration!')
    tm = j2_env.get_template("templates/signup_teacher.html")
    content_html = tm.render(name=f'{teacher.full_name}')
    message.attach(MIMEText(content_html, "html"))
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
  except Exception as e:
    logger.info(f'error: {e}')


def sign_up_teacher_successful(email, teacher):
  try:
    receiver_email = email
    context = ssl.create_default_context()
    message = set_header_email(receiver_email, 'Thank you for your registration!')
    tm = j2_env.get_template("templates/signup_teacher_successful.html")
    content_html = tm.render(name=f'{teacher.full_name}', email=f'{teacher.email}')
    message.attach(MIMEText(content_html, "html"))
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
  except Exception as e:
    logger.info(f'error: {e}')


def add_course(email, obj):
  try:
    receiver_email = email
    context = ssl.create_default_context()
    message = set_header_email(receiver_email, obj["course_name"])
    tm = j2_env.get_template("templates/add_course.html")
    content_html = tm.render(teacher_url_avatar=f'{obj["teacher_url_avatar"]}', teacher_name=f'{obj["teacher_name"]}',
                             course_name=f'{obj["course_name"]}',
                             course_url_intro_video=f'{obj["course_url_intro_video"]}')
    message.attach(MIMEText(content_html, "html"))
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
  except Exception as e:
    logger.info(f'error: {e}')


def uninstall(email, obj):
  try:
    receiver_email = email
    context = ssl.create_default_context()
    message = set_header_email(receiver_email, f'Tạm dừng phát hành: {obj["course_name"]}')
    tm = j2_env.get_template("templates/uninstall.html")
    content_html = tm.render(name=f'{obj["name"]}',
                             course_name=f'{obj["course_name"]}')
    message.attach(MIMEText(content_html, "html"))
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
  except Exception as e:
    logger.info(f'error: {e}')

def release_email(email, obj):
  try:
    receiver_email = email
    context = ssl.create_default_context()
    message = set_header_email(receiver_email, f'Khắc phục sự cố: {obj["course_name"]}')
    tm = j2_env.get_template("templates/release.html")
    content_html = tm.render(name=f'{obj["name"]}',
                             course_name=f'{obj["course_name"]}')
    message.attach(MIMEText(content_html, "html"))
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
  except Exception as e:
    logger.info(f'error: {e}')


def transfer_successful(email, full_name, transaction, transaction_courses):
  try:
    receiver_email = email
    context = ssl.create_default_context()
    message = set_header_email(receiver_email, 'Transfer successful!')
    tm = j2_env.get_template("templates/transfer_successful.html")
    content_html = tm.render(full_name=full_name, transaction_courses=transaction_courses, transaction=transaction)
    message.attach(MIMEText(content_html, "html"))
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
  except Exception as e:
    logger.info(f'error: {e}')
