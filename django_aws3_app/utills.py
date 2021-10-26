from storages.backends.s3boto3 import S3Boto3Storage

class s3_setup:
    # AWS Configuration
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_STORAGE_BUCKET_NAME = ''
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_REGION_NAME = 'us-east-2'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    AWS_S3_VERIFY = True
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

def upload_img_to_s3(id, file_name):
    if file_name:
        img_path = "Profile/{}/BookBox/Image/{}".format(id, file_name)
    else:
        img_path = "Profile/{}/BookBox/Image".format(id)
    return img_path


def upload_file_to_s3(id, file_name):
    if file_name:
        file_path = f"Documets/{id}/BookBox/File/{file_name}"
    else:
        file_path = f"Documets/{id}/BookBox/File"
    return file_path

'''
class StaticStorage(S3Boto3Storage):
    bucket_name = 'my-app-bucket'
    location = 'static'

class crud_s3(S3Boto3Storage):
    def get():
        pass
    
    def post():
        pass 
        
    def put():
        pass
    
    def delete():
        pass
'''