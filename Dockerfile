FROM python:3.8.10-slim-buster
LABEL "org.opencontainers.image.authors"="John Bradley <john.bradley@duke.edu>"
LABEL "org.opencontainers.image.description"="Tool to reformat drexel metadata JSON files"

WORKDIR /pipeline

# ADD scripts in /pipeline to the PATH
ENV PATH="/pipeline:${PATH}"

COPY dm_formatter.py /pipeline
CMD echo "dm_formatter.py input output"
