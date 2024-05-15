from boto3 import resource
import config


s3 = resource("s3", endpoint_url=config.S3_STORAGE_URL)
bucket = s3.Bucket(config.BUCKET_NAME)
