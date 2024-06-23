import config.broker as config
from celery import Celery

app = Celery(__name__, broker=f"amqp://{config.HOST}:{config.PORT}")
app.config_from_object("tasks.celeryconfig")

from . import tasks  # noqa
