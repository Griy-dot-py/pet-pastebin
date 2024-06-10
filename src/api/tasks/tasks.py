from celery import Task
from . import app
from classes.abc import PasteProtocol


@app.task(serializer="pickle")
def del_paste(paste: PasteProtocol):
    paste.delete()


del_paste: Task
