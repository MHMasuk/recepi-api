FROM python:3.7-alpine
MAINTAINER MHMasuk

ENV PYTHONUNBUFFERED 1

copy ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
copy ./app /app

RUN adduser -D user
USER user
