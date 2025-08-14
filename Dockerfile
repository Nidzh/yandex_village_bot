FROM python:3.12-slim as requirements-stage

RUN pip install poetry==1.8.0

COPY ./pyproject.toml ./poetry.lock* /

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12

# Установка локалей
RUN apt-get update && apt-get install -y --no-install-recommends locales \
    && echo "ru_RU.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

# Установка переменных окружения
ENV LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU:ru \
    LC_ALL=ru_RU.UTF-8

WORKDIR /app
COPY --from=requirements-stage /requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD alembic upgrade head && python run.py