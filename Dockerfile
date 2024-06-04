FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app/

ADD ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app/

