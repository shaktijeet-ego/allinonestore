from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path("<single_slug>",views.single_slug, name="single_slug"),
    #path('products/<int:id>',views.products_detail, name = "detail"),
   #path('products/<int:id>', views.shop_products, name='shop-products'),
   
    
]