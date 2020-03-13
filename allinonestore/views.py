from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

from products.models import Product



def homepage(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products':products})


def about(request):
    return render(request, 'about.html')





def contact(request):
    if request.method == 'POST':
        message = request.POST['name']

        send_mail('Contact Form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['shaktijeet.tripathi@gmail.com'],
                  fail_silently=False)
    return render(request, 'contact.html')
