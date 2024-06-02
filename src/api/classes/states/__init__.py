from .uploaded import Uploaded
from .draft import Draft
from .restored import Restored

from aws import Cloud
from database import Database
from cache import HashCache, DataCache


def init_sources(cloud: Cloud,
    db: Database,
    hash_cache: HashCache,
    text_cache: DataCache,
    metadata_cache: DataCache
) -> None:
    Draft.cloud = cloud
    Draft.db = db
    Draft.cache = hash_cache
    
    Restored.cloud = cloud
    Restored.db = db
    Restored.text_cache = text_cache
    Restored.metadata_cache = metadata_cache
