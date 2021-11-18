FROM python:3.9.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django_kornilov

COPY requirements.txt .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]