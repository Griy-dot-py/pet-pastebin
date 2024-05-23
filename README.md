# Development README

### Run application:
```
docker compose -f Docker/docker-compose.yml --env-file config/.env up --build
```
### Access api:
```
docker compose -f Docker/docker-compose.yml exec api bash
```