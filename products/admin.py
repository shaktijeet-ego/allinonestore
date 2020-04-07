from django.contrib import admin
from .models import Shop, ShopType, Product, ShopProduct

# Register your models here.
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ShopProduct)
admin.site.register(ShopType)