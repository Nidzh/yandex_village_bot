from typing import BinaryIO

import boto3
from botocore.client import Config

S3_ENDPOINT = "https://s3.mtatsminda.dev/"
S3_ACCESS_KEY = "Ot2yKObwDsrY1NaLclWr"
S3_SECRET_KEY = "RVOD8aSF20gPoJoiCxOHPJuhbU0uCJ3BFkPyDk45"
S3_BUCKET = "yandex-village"

S3 = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    config=Config(signature_version="s3v4"),
)


def upload_fileobj_to_s3(fileobj: BinaryIO, key: str, content_type: str = "image/jpeg") -> str:
    """
    Загружает file-like объект в S3 без сохранения на диск.
    """
    fileobj.seek(0)
    S3.upload_fileobj(
        Fileobj=fileobj,
        Bucket=S3_BUCKET,
        Key=key,
        ExtraArgs={"ContentType": content_type},
    )
    return key
