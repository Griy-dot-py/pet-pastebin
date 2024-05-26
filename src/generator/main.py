from redis import Redis
from config import HASH_CACHE_HOST, HASH_CACHE_PORT
from sequence import UniqueNumberSequence


if __name__ == "__main__":
    with Redis(host=HASH_CACHE_HOST, port=HASH_CACHE_PORT) as redis:
        seq = UniqueNumberSequence(storage=redis, recomended_size=5)
        seq.start_loop()
