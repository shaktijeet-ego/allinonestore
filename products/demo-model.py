from django.db import models

# Create your models here.

# For shop in the beginning


# class ShopType(models.Model):
#     shop_type = models.CharField(max_length=50)
#     shop_type_description = models.TextField()

#     def __str__(self):
#         return self.shop_type


class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    shop_location = models.CharField(max_length=100)
    shop_opening_time = models.CharField(max_length=10)
    shop_slug = models.CharField(max_length = 20)
    # shop_type = models.ForeignKey(
    #     ShopType, default=1, on_delete=models.SET_DEFAULT)
    shop_image = models.ImageField(upload_to='products', null=True, blank=True)
    shop_owner = models.CharField(max_length=100)
    shop_description = models.TextField()
    shop_added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shop_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_image = models.ImageField(
        upload_to='products', null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_slug = models.CharField(max_length = 20)
    product_added_date = models.DateTimeField(auto_now=True)
    shop_name = models.ForeignKey(
        Shop, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.product_name


class ProductDetails(models.Model):
    product_name = models.ForeignKey(
        Product, default=1, on_delete=models.SET_DEFAULT)
    test_something = models.CharField(max_length=20)

    def __str__(self):
        return self.test_something
