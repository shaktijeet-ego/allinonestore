from django.db import models
from datetime import datetime

# change names away from tutorial_... 
class Shop(models.Model):
    tutorial_category = models.CharField(max_length=100)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)
    shop_image = models.ImageField(upload_to='products', null=True, blank=True)
    shop_owner = models.CharField(max_length=100)
    shop_description = models.TextField()
    shop_added_date = models.DateTimeField(auto_now=True)

    class Meta:
        # Django doesn't handle plurals well
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category


class Product(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(Shop, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    product_image = models.ImageField(
        upload_to='products', null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    # on_delete will set the categories of a deleted category to default
    
    series_summary = models.CharField(max_length=300)
    
    class Meta:
        # Django doesn't handle plurals well
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series



class ProductDetails(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default=datetime.now)
    tutorial_image = models.ImageField(
        upload_to='products', null=True, blank=True)

    tutorial_series = models.ForeignKey(Product, default=1,verbose_name="Series", on_delete=models.SET_DEFAULT )
    tutorial_slug = models.CharField(max_length=200, default=1)

    # converts objects to strings so they can be passed more easily to HTML
    def __str__(self):
        return self.tutorial_title