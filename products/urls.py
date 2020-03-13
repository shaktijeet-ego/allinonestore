from django.urls import path
from . import views

urlpatterns = [
    path('<slug>',views.products_detail, name = "detail")
]