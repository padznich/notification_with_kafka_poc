FROM python:3.10-slim as base


ARG ARGS_GIT_BRANCH="not set"
ARG ARGS_GIT_COMMIT_HASH="not set"

ENV  \
    # python
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # django
    DJANGO_ENVIRONMENT=development \
    # project
    APP_PATH="/app"

ENV APP_GIT_BRANCH ${ARGS_GIT_BRANCH}
ENV APP_GIT_COMMIT_HASH ${ARGS_GIT_COMMIT_HASH}

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait
RUN python -m pip install --upgrade pip

RUN apt-get update  \
    && apt-get install --no-install-recommends -y \
    build-essential \
    postgresql-client  \
    libssl-dev  \
    && pip install poetry

ADD pyproject.toml pyproject.toml
ADD poetry.lock poetry.lock
RUN poetry config virtualenvs.create false && poetry install --without dev

COPY /src $APP_PATH
COPY /config /config
WORKDIR $APP_PATH


##############################################################################
# DEV
##############################################################################
FROM base as dev
RUN poetry install --with dev

##############################################################################
# PROD
##############################################################################
FROM base as prod
ENV DJANGO_ENVIRONMENT=production