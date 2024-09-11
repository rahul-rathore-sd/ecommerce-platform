# from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/', blank=True, null=True)

    def __str__(self):
        return self.name

class Categorylogo(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='categorylogo/', blank=True, null=True)
    
    def __str__(self):
        return self.name
