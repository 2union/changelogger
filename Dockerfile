FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE changelogger.settings
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
