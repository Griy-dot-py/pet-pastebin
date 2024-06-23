from datetime import datetime
from os import PathLike
from typing import Optional

from botocore.exceptions import ClientError
from mypy_boto3_s3.service_resource import Bucket


class Cloud(object):
    PATH = "/users/{user_id}/{name}"
    FILENAME_FORMAT = "%Y-%m-%d_%H:%M:%S"

    def __init__(self, bucket: Bucket) -> None:
        self._bucket = bucket

    def upload(self, text: str, user_id: Optional[int] = None) -> PathLike:
        if user_id is None:
            user_id = "guest"
        path = self.PATH.format(
            user_id=user_id, name=datetime.now().strftime(self.FILENAME_FORMAT)
        )
        self._bucket.Object(path).put(Body=text)
        return path

    def download(self, path: PathLike) -> Optional[str]:
        try:
            response = self._bucket.Object(path).get()
        except ClientError:
            return None
        content = response["Body"].read()
        return content.decode()

    def delete(self, path: PathLike) -> None:
        self._bucket.Object(path).delete()
