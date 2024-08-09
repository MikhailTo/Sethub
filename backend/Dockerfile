# Используем базовый образ Python
FROM python:3.12.1-alpine3.19

# Отключаем запись байт-кода Python
ENV PYTHONDONTWRITEBYTECODE 1 
# Отключаем буферизацию вывода
ENV PYTHONUNBUFFERED 1 

ENV POETRY_VIRTUALENVS_CREATE=false

# https://python-poetry.org/docs/configuration/#using-environment-variables
# https://gist.github.com/soof-golan/6ebb97a792ccd87816c0bda1e6e8b8c2
# Configure Poetry
ENV POETRY_VERSION=1.8.3 
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv 

# Tell Poetry where to place its cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache 

# Creating a virtual environment just for poetry and install it with pip
RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools \
	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# RUN pip install --upgrade pip

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Устанавливаем рабочую директорию
WORKDIR /usr/src/sethub

# Install dependencies
COPY poetry.lock pyproject.toml ./

# [OPTIONAL] Validate the project is properly configured
RUN poetry check

RUN apk update \
    && apk add postgresql-client build-base postgresql-dev libpq-dev

# Install Dependencies
RUN poetry install --no-interaction --no-cache --no-dev
# RUN poetry install --no-dev

# COPY requirements.txt /temp/requirements.txt
# RUN pip install -r /temp/requirements.txt




COPY . .

EXPOSE 8000

RUN mkdir -p /usr/src/sethub/frontend/static
RUN mkdir -p /usr/src/sethub/frontend/media

RUN chown -R 1000:1000 /usr/src/sethub/frontend/media

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

CMD ["./docker-entrypoint.sh"]

RUN adduser --disabled-password sethub
USER sethub