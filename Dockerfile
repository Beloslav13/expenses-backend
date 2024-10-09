FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update && apt install nano

COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /app/