from os import PathLike
from aws import bucket


def download_from_cloud(path: PathLike) -> str:
    response = bucket.Object(path).get()
    content = response["Body"].read()
    return content.decode()
