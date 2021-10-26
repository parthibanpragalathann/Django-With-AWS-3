from django.db import models


class book_box(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.IntegerField(max_length=10)
    pic = models.ImageField()
    document = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Book Boxes'