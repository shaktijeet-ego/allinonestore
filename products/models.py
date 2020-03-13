from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length= 1000 ) 
    slug = models.SlugField()
    product_image = models.ImageField(upload_to = 'products', null = True, blank = True)
    price = models.FloatField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name