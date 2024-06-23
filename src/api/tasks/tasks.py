from celery import Task
from classes.abc import PasteProtocol

from . import app


@app.task(serializer="pickle")
def del_paste(paste: PasteProtocol):
    paste.delete()


del_paste: Task
