from django.shortcuts import render
from .models import Product

# Create your views here.


def products_detail(request):
    products = Product.objects.all().order_by('date')
    return render(request,'products/product_details.html',{'products':products})
