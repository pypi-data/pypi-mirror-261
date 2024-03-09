import boto3
import requests
from io import BytesIO


class AmazonS3:
    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str) -> None:
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.s3_raw_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def _check_acl(self, acl: str) -> None:
        """
        :param acl: https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl
        :return: None
        """
        valid_acl = ["private", "public-read", "public-read-write", "authenticated-read", "aws-exec-read",
                     "bucket-owner-read", "bucket-owner-full-control", "log-delivery-write"]

        if acl and acl not in valid_acl:
            raise ValueError(
                f"Invalid ACL: {acl}. Please check the https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl for valid ACLs.")

    def upload_from_local_file(self, file_path: str, bucket_name: str, object_name: str, acl: str = "public-read",
                               bucket_domain: str = "") -> str:
        """
        :param file_path: 本地文件的绝对路径。
        :param bucket_name: S3 bucket的名称。
        :param object_name: S3中的目标文件的Key。例如a/b.txt为a文件夹下的b.txt文件
        :param acl: S3文件的权限。默认为public-read。
        :param bucket_domain: S3 bucket的域名，用于替换默认返回链接。例如s3.yourdomain.com。
        :return: 文件的公开URL。
        """
        self.s3_raw_client.upload_file(
            file_path,
            bucket_name,
            object_name,
            ExtraArgs={"ACL": acl}
        )

        # 构造图像在 S3 的公开访问链接
        public_url = f"https://{bucket_domain}/{object_name}" if bucket_domain else f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        return public_url

    def upload_from_url(self, url, bucket_name, object_name, acl="public-read", bucket_domain=""):
        """
        下载文件，并上传到S3，返回文件的公开URL。
        :param url: 要下载的文件的URL。
        :param bucket_name: S3 bucket的名称。
        :param object_name: S3中的目标文件的Key。例如a/b.txt为a文件夹下的b.txt文件
        :param acl: S3文件的权限。默认为public-read。
        :param bucket_domain: S3 bucket的域名，用于替换默认返回链接。例如s3.yourdomain.com。
        """
        response = requests.get(url)
        response.raise_for_status()
        self.s3_raw_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=BytesIO(response.content),
            ACL=acl
        )

        # 构造图像在 S3 的公开访问链接
        public_url = f"https://{bucket_domain}/{object_name}" if bucket_domain else f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        return public_url
