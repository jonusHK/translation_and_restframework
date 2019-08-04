from storages.backends.s3boto3 import S3Boto3Storage
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    bucket_name = 'media-api-dstagram.wpsshool.site'

    region_name = 'ap-northeast-2'
    # custom_domain = 's3.%s.amazonaws.com/%s' % (region_name, bucket_name)
    custom_domain = bucket_name