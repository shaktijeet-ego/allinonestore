from django.contrib import admin
from .models import Shop, Product,TutorialSeries

# Register your models here.
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(TutorialSeries)
#admin.site.register(ShopProduct)
#admin.site.register(ShopType)