# syntax=docker/dockerfile:1


#Base image
FROM python:3.8-slim-buster AS base

# Setting a working directory
WORKDIR /application

# Prevents Python from writing pyc files to disc 
ENV PYTHONDONTWRITEBYTCODE 1
# Prevents Python from buffering stdout and stderr 
ENV PYTHONFAULTHANDLER 1


RUN pip install --upgrade pip && pip install pipenv

RUN apt-get update && apt-get install -y netcat --no-install-recommends

# Installing Dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc


COPY ./Pipfile* /application/

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy


# Copy project
COPY . /application/

ENTRYPOINT [ "/application/entrypoint.sh" ]
