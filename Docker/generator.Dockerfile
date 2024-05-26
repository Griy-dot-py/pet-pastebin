FROM python:3.11.9

WORKDIR /app/
COPY src/generator/requirements.txt .
RUN pip install -r requirements.txt
COPY config/.env .env
COPY src/generator .

ENTRYPOINT ["python3"]
CMD ["main.py"]
