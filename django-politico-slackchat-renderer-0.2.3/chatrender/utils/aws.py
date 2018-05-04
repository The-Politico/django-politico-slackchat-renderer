import botocore

import boto3
from chatrender.conf import settings


def get_bucket():
    session = boto3.session.Session(
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    s3 = session.resource('s3')

    return s3.Bucket(settings.AWS_S3_BUCKET)


def get_cloudfront_client():
    if settings.AWS_CLOUDFRONT_DISTRIBUTION:
        return boto3.client(
            'cloudfront',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
    else:
        return None


def check_object_exists(obj):
    bucket = get_bucket()
    try:
        bucket.Object(obj).load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return False
        else:
            raise botocore.exceptions.ClientError()
    return True


class Defaults(object):
    CACHE_HEADER = str('max-age=300')
    ACL = 'public-read'


defaults = Defaults
