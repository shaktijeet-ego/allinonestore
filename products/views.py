from django.shortcuts import render
from products.models import Product

# Create your views here.
def Home(request):
    return render(request, 'products/home.html')