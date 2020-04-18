from django.contrib import admin
from .models import Shop, Product,ProductDetails

# Register your models here.
admin.site.register(Shop)
admin.site.register(Product)
#admin.site.register(ShopType)
admin.site.register(ProductDetails)
#admin.site.register(ShopProduct)
#admin.site.register(ShopType)