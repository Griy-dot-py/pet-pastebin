FROM python:3.11.9

WORKDIR /aws/
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["flask"]
CMD ["--app", "src/api/resources", "run", "--port", "5000", "--host", "0.0.0.0"]
