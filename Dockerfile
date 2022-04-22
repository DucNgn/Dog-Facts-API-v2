FROM python:3.8

RUN mkdir /app
WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml /app
RUN poetry install --no-dev

COPY ./ /app

EXPOSE 8000
