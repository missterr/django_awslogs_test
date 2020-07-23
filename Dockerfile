# Base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set up a workdir
RUN mkdir /django_awslogs_test
WORKDIR /django_awslogs_test

# Install dependencies
COPY requirements.txt /django_awslogs_test/
RUN pip install -r /django_awslogs_test/requirements.txt

ADD /django_awslogs_test/ /django_awslogs_test/