import config.aws as config
from boto3 import resource

from .cloud import Cloud

s3 = resource(
    "s3",
    region_name=config.REGION,
    endpoint_url=config.URL,
    aws_access_key_id=config.ACCESS_KEY_ID,
    aws_secret_access_key=config.SECRET_ACCESS_KEY,
)
bucket = s3.Bucket(config.BUCKET_NAME)

cloud = Cloud(bucket=bucket)
