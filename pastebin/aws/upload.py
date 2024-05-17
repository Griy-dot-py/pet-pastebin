from os import PathLike
from aws import bucket
from datetime import datetime


PATH = "users/{user_id}/{datetime}"
FORMAT = "%Y-%m-%d_%H:%M:%S"


def upload_to_cloud(text: str, user_id: int) -> PathLike:
    path = PATH.format(user_id=user_id, datetime=datetime.now().strftime(FORMAT))
    bucket.put_object(Key=path, Body=text)
    return path
