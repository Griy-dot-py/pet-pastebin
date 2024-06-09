from celery import Celery
import config.broker as config


app = Celery(__name__, broker=f"amqp://{config.HOST}:{config.PORT}")
