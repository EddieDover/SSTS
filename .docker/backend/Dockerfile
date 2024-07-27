FROM python:3.11.9-alpine as builder

ENV POETRY_CACHE_DIR='/root/.cache/pypoetry' \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_NO_INTERACTION=1


WORKDIR /api

COPY backend/poetry.lock .
COPY backend/pyproject.toml .

RUN apk update && apk add --no-cache postgresql build-base gcc libpq libpq-dev

RUN pip install poetry==1.8.3

RUN poetry install


FROM python:3.11.9-alpine as runner

ENV DEPENDENCY_DIR=/usr/local/lib/python3.11/site-packages/

WORKDIR /api

RUN apk update && apk add --no-cache postgresql libpq

COPY backend/src .

COPY --from=builder $DEPENDENCY_DIR $DEPENDENCY_DIR