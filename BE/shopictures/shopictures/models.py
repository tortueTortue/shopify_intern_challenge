from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='images_repository')