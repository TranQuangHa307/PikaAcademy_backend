import os
from datetime import timedelta

CURRENT_ENV = os.environ.get('ENVIRONMENT')
SENTRY_DNS = os.environ.get('SENTRY_DNS', 'https://b3cafe9cdfed4d078b282149eedf07be@o961745.ingest.sentry.io/5910130')
RELEASE_VERSION = os.environ.get('RELEASE_VERSION', '0.0.1')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                         'mysql+pymysql://root:Anhhoang@123@localhost:3306/pikaacademy?charset=utf8mb4')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"

CORS_MAX_AGE = 7776000  # 3 months
CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "").split(",")
CORS_ORIGINS = list(set(CORS_ORIGINS))
if "" in CORS_ORIGINS:
  CORS_ORIGINS.remove("")
ACCESS_TOKEN_DROPBOX = 'XexPqeot4JQAAAAAAAAAAZcEKNZe3oeS-7RPqadNAwu65KjOQZQnSlhV_AwE9kJg'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
SENDGRID_API_KEY = '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'

# smtp
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "pikaacademy.edu@gmail.com"
password = 'Anhhoang@123'
