from boto3 import resource
import config


s3 = resource(
    "s3",
    region_name=config.REGION_NAME,
    endpoint_url=config.S3_STORAGE_URL,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
)
bucket = s3.Bucket(config.BUCKET_NAME)
