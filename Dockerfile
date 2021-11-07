FROM python:3.7

WORKDIR /home/app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN find . -type f -name "*.py[co]" -delete
RUN find . -type d -name "__pycache__" -delete
ADD . ./
