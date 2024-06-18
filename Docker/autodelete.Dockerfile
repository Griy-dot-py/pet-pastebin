FROM python:3.12

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://install.python-poetry.org | python
RUN poetry self update

WORKDIR /aws/
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

WORKDIR /app/
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --only main,queue
COPY config/.env .env
COPY docs/ docs/
COPY src/api .

ENV C_FORCE_ROOT="yes" 
ENTRYPOINT ["poetry", "run", "celery", "-A", "tasks", "worker"]
