FROM python:3.12.1-alpine3.19

WORKDIR /usr/src/sethub/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION="1.8.3"
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/venv/bin:${PATH}"

COPY poetry.* pyproject.toml ./
RUN poetry install --no-dev

COPY . /usr/src/sethub/backend
EXPOSE 8000

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait
CMD ["./docker-entrypoint.sh"]