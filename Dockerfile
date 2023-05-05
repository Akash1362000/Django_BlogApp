FROM python:3.11-slim-buster
ENV PYTHONBUFFERED=1
WORKDIR /blog_app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
