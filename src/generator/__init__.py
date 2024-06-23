import config.hash_cache as config
from database import sequence
from main import HashGenerator
from redis import Redis

if __name__ == "__main__":
    with Redis(host=config.HOST, port=config.PORT) as redis:
        gen = HashGenerator(storage=redis, recomended_size=5, iterator=sequence)
        gen.start()
