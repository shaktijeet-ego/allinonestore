from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    #path('products/<int:id>',views.products_detail, name = "detail"),
    path('products/<int:id>', views.shop_products, name='shop-products'),
   
    
]