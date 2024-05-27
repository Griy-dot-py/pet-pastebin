from redis import Redis
from config import HASH_CACHE_HOST, HASH_CACHE_PORT

from .hash import HashCache


hash_redis = Redis(host=HASH_CACHE_HOST, port=HASH_CACHE_PORT)
hash_cache = HashCache(cache=hash_redis)
