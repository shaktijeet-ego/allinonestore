from django.db import models

# Create your models here.

#For shop in the beginning


class ShopType(models.Model):
    shop_speciality = models.CharField(max_length = 50)

    def __str__(self):
        return self.shop_speciality



class Shop(models.Model):
    shop = models.CharField(max_length = 50)
    shop_location = models.CharField(max_length = 100)
    shop_opening_time = models.CharField(max_length = 5)
    shop_speciality = models.ForeignKey(ShopType, default = "None", on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to = 'products', null = True, blank = True)
    shop_image = models.ImageField(upload_to = 'products', null =True, blank = True)
     
    def __str__(self):
            return self.shop

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length= 1000 ) 
    slug = models.SlugField()
    product_image = models.ImageField(upload_to = 'products', null = True, blank = True)
    price = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey(Shop, default = "None", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
 
class ShopProduct(models.Model):
    name = models.ForeignKey(Shop, default = "None", on_delete=models.CASCADE)
    product_name = models.TextField(max_length= 1000)

    def __str__(self):
        return self.name



