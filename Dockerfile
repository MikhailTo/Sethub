# Стартовый образ
FROM python:3.12.1-alpine3.19

WORKDIR /usr/src/sethub

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-client build-base postgresql-dev libpq-dev

RUN pip install --upgrade pip
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

COPY . .

EXPOSE 8000

RUN mkdir -p /usr/src/sethub/frontend/static
RUN mkdir -p /usr/src/sethub/frontend/media

RUN chown -R 1000:1000 /usr/src/sethub/frontend/media

RUN adduser --disabled-password sethub
USER sethub

# ENTRYPOINT ["/usr/src/sethub/backend/docker-entrypoint.sh"]