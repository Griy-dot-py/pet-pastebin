# Development README

### Run application:
```
docker compose -f Docker/docker-compose.yml --env-file config/.env up --build
```
### Run frontend:
```
docker build -t pastebin-front -f Docker/front.Dockerfile.
```
### Running services separately:
##### broker:
```
docker run --name pastebin-broker --restart unless-stopped -d -p 5672:5672 rabbitmq:3.13.3
```
##### database:
```
docker run --name pastebin-database -e POSTGRES_DB=pastebin -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d --restart unless-stopped postgres:14.12
```
##### sequence:
```
docker run --name pastebin-sequence -e POSTGRES_DB=pastebin -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5433:5432 -d --restart unless-stopped postgres:14.12
```
##### hashcache:
```
docker run --name pastebin-hashcache -d -p 6380:6379 --restart unless-stopped redis:7.0.15-alpine
```
##### metadatacache:
```
docker run --name pastebin-metadatacache -d -p 6381:6379 --restart unless-stopped redis:7.0.15-alpine
```
##### textcache:
```
docker run --name pastebin-textcache -d -p 6382:6379 --restart unless-stopped redis:7.0.15-alpine
```
##### generator:
! copy .env into src/generator
```
cd src/generator
poetry run python3 main.py &
```
##### autodelete:
! copy .env into src/api
```
cd src/api
poetry run celery -A tasks worker
```
##### api:
configure APIDOCS_PATH in .env
! copy .env into src/api
```
cd src/api
poetry run gunicorn -w 4 -b 0.0.0.0:8000 resources:app
```
##### server:
```
docker build -t pastebin-server -f Docker/server.Dockerfile .
docker run --name pastebin-server -p 80:80 --restart unless-stopped -d pastebin-server
```
