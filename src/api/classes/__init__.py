from . import abc
from . import states

from database import paste_db
from aws import cloud
from cache import hash_cache


states.init_sources(cloud=cloud, db=paste_db, hash_cache=hash_cache)


from .main import Paste
