import config.hash_cache as hash_config
import config.metadata_cache as metadata_config
import config.text_cache as text_config
from redis import Redis

from .data import DataCache
from .hash import HashCache

hash_redis = Redis(host=hash_config.HOST, port=hash_config.PORT)
hash_cache = HashCache(cache=hash_redis)

text_redis = Redis(host=text_config.HOST, port=text_config.PORT)
text_cache = DataCache(cache=text_redis)

metadata_redis = Redis(host=metadata_config.HOST, port=metadata_config.PORT)
metadata_cache = DataCache(cache=metadata_redis)
