from django.db import models

# Create your models here.

#For shop in the beginning

class Shop(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tutorial_category


class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(Shop, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series


# Create your models here.
class Product(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	#tutorial_published = models.DateTimeField("date published", default=datetime.now())

	tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)
	
	def __str__(self):
		return self.tutorial_title



















# class Shop(models.Model):  #Category
#     shop = models.CharField(max_length = 50)
#     shop_location = models.CharField(max_length = 100)
#     shop_opening_time = models.CharField(max_length = 5)
#     shop_slug = models.CharField(max_length=200,default=1)
#     #shop_speciality = models.ForeignKey(ShopType, default = "None", on_delete=models.CASCADE)
#     product_image = models.ImageField(upload_to = 'products', null = True, blank = True)
#     shop_image = models.ImageField(upload_to = 'products', null =True, blank = True)
     
#     def __str__(self):
#             return self.shop        

# class Product(models.Model):
#     name = models.CharField(max_length = 50)
#     description = models.TextField(max_length= 1000 ) 
#     slug = models.SlugField()
#     product_image = models.ImageField(upload_to = 'products', null = True, blank = True)
#     price = models.FloatField()
#     date = models.DateTimeField(auto_now=True)
#     shop = models.ForeignKey(Shop, default = "None", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name



# """ class ShopType(models.Model):
#     shop_speciality = models.CharField(max_length = 50)

#     def __str__(self):
#         return self.shop_speciality



# class ShopProduct(models.Model):
#     name = models.ForeignKey(Shop, default = "None", on_delete=models.CASCADE)
#     product_name = models.TextField(max_length= 1000)

#     def __str__(self):
#         return self.name


 
# class ShopProduct(models.Model):
#     name = models.ForeignKey(Shop, default = "None", on_delete=models.CASCADE)
#     product_name = models.TextField(max_length= 1000)

#     def __str__(self):
#         return self.name
#  """


