FROM python:3.10-alpine

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2


COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt


COPY . /app/
RUN adduser -D myuser
USER myuser

CMD gunicorn newsData.wsgi:application