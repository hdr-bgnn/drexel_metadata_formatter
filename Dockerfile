FROM python:3.8.10-slim-buster

WORKDIR /pipeline

COPY dm_formatter.py /pipeline
CMD echo "python dm_formatter.py input output"
