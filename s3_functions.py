import boto3
from s3_info import s3



def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def list_files(bucket):
    s3_client = boto3.client('s3')
    contents = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            # print(item)
            contents.append(item)
    except Exception as e:
        pass
    return contents

def list_image(bucket):
    bucket = s3.Bucket(bucket)
    public_urls = []
    try:
        for obj in bucket.objects.all():
            public_urls.append(obj.key)
    except Exception as e:
        pass
    # print("[DATA] : The contents inside show_image = ", public_urls)
    return public_urls