from django.db import models
from django_aws3_app.utills import upload_img_to_s3, upload_file_to_s3

class book_box(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField(max_length=10)
    profile = models.ImageField(upload_to=upload_img_to_s3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Book Boxes'