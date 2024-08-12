from django.db import models
from  . import book
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)

    def __str__(self):
        return self.name
