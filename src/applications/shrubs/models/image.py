from django.conf import settings
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


def upload_to(instance: "ShrubsImage", filename):
    return f"{settings.AWS_S3_IMAGE_LOCATION}/img__{instance.pk}__{filename}"


class ShrubsImage(models.Model):
    shrubs = models.OneToOneField("Shrubs", on_delete=models.CASCADE, primary_key=True)
    original = models.FileField(storage=S3Boto3Storage(), upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        msg = f"shrubs{self.shrubs}"
        return msg