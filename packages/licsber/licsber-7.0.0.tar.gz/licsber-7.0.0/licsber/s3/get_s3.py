import boto3
from botocore.config import Config


def get_s3(endpoint, access_key, secret_key, region='cn', ssl=False):
    return boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region,
        use_ssl=ssl,
        endpoint_url=endpoint,
        config=Config(s3={'addressing_style': 'path', 'signature_version': 's3v4'}),
    )
