FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_IN_PROJECT 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

COPY . /app/

EXPOSE 8080


RUN uv sync
RUN uv run python manage.py makemigrations
RUN uv run python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
