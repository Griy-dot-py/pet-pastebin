FROM python:3.12

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://install.python-poetry.org | python
RUN poetry self update

WORKDIR /app/
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --only main
COPY config/.env .env
COPY src/generator .

ENTRYPOINT ["poetry", "run", "python3"]
CMD ["__init__.py"]
