FROM python:3.11.9

WORKDIR /aws/
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

WORKDIR /app/src/api/
ENTRYPOINT ["gunicorn", "-w", "4"]
CMD ["-b", "0.0.0.0", "resources:app"]
