# pull official base image
FROM python:3.10.1-slim-buster

# Create a working directory
RUN mkdir -p /usr/src/app

# set working directory
WORKDIR /usr/src/app

# set the environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# install python dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt 

# add app
COPY . .
