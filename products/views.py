from django.shortcuts import render,get_object_or_404
from .models import Shop,ShopType,Product,ShopProduct

# Create your views here.

def homepage(request):
    products = Shop.objects.all()
    return render(request, 'products/shop.html',{'products':products})

def shop_products(request, id):
    shops = Product.objects.all()
    return render(request, 'products/shop_products.html', {'shops': shops})

# def product_details(request, id):
#     product_detail = get_object_or_404(Product, pk = id)
#     return render(request, 'products/product_details.html', {'product':product_detail})
