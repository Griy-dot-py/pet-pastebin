# Development README

### Run application:
```
docker compose -f Docker/docker-compose.yml --env-file config/.env up --build
```
### Access api:
```
docker compose -f Docker/docker-compose.yml exec api bash
```
### Running services separately:
##### database:
```
docker run --name pastebin-database -e POSTGRES_DB=pastebin -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d --restart unless-stopped postgres:14.12
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
src/generator$ python3 main.py &
```
##### server:
```
docker build -t pastebin-server -f Docker/server.Dockerfile .
docker run -p 80:80 --restart unless-stopped -d pastebin-server
```