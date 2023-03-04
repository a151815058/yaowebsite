import boto3

s3 = boto3.resource('s3',
                    aws_access_key_id='AKIA4QRVWAW3ELRWH7WZ',
                    aws_secret_access_key= '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'
                    )
bucket = s3.Bucket('yaoweb')

a=[]


print(a[3])