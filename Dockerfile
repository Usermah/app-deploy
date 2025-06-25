FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install required system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libkrb5-dev \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
