from typing import BinaryIO, Iterator, Tuple, List
from io import BytesIO
import os
import boto3
from botocore.client import Config

S3_ENDPOINT = "https://s3.mtatsminda.dev/"
S3_ACCESS_KEY = "Ot2yKObwDsrY1NaLclWr"
S3_SECRET_KEY = "RVOD8aSF20gPoJoiCxOHPJuhbU0uCJ3BFkPyDk45"
S3_BUCKET = "yandex-village"
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff")

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

def iter_bucket_photos(prefix: str = "") -> Iterator[Tuple[str, BytesIO]]:
    """
    Итерируется по всем объектам в бакете (с префиксом, если указан),
    отдает только изображения. Данные возвращаются как BytesIO (без диска).
    """
    paginator = S3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=S3_BUCKET, Prefix=prefix):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            if not key.lower().endswith(IMAGE_EXTS):
                continue
            resp = S3.get_object(Bucket=S3_BUCKET, Key=key)
            body = resp["Body"]  # StreamingBody
            buf = BytesIO(body.read())
            buf.seek(0)
            yield key, buf


def download_all_photos_to_dir(dest_dir: str, prefix: str = "") -> List[str]:
    """
    Скачивает все фото из бакета в локальную папку dest_dir.
    Возвращает список локальных путей.
    """
    os.makedirs(dest_dir, exist_ok=True)
    saved_paths: List[str] = []
    for key, buf in iter_bucket_photos(prefix=prefix):
        # сохраняем под тем же именем (с учетом возможных подпапок в key)
        local_path = os.path.join(dest_dir, *key.split("/"))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "wb") as f:
            f.write(buf.getbuffer())
        saved_paths.append(local_path)
    return saved_paths


def list_photo_presigned_urls(expires_in: int = 3600, prefix: str = "") -> List[str]:
    """
    Возвращает список presigned URL для всех фоток (удобно, если не нужно качать).
    """
    urls: List[str] = []
    paginator = S3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=S3_BUCKET, Prefix=prefix):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            if not key.lower().endswith(IMAGE_EXTS):
                continue
            url = S3.generate_presigned_url(
                "get_object",
                Params={"Bucket": S3_BUCKET, "Key": key},
                ExpiresIn=expires_in,
            )
            urls.append(url)
    return urls

if __name__ == "__main__":
   # 2) Сохранить всё в папку ./photos
    paths = download_all_photos_to_dir("./photos")