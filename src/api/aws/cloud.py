from os import PathLike
from datetime import datetime

from mypy_boto3_s3.service_resource import Bucket


class Cloud(object):
    PATH = "/users/{user_id}/{name}"
    FILENAME_FORMAT = "%Y-%m-%d_%H:%M:%S"
    
    def  __init__(self, bucket: Bucket) -> None:
        self._bucket = bucket
    
    def upload(self, text: str, user_id: int) -> PathLike:
        path = self.PATH.format(
            user_id=user_id,
            name=datetime.now().strftime(self.FILENAME_FORMAT)
        )
        self._bucket.Object(path).put(
            Body=text
        )
        return path
    
    def download(self, path: PathLike) -> str:
        response = self._bucket.Object(path).get()
        content = response["Body"].read()
        return content.decode()