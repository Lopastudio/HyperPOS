from django.urls import path
from . import views

urlpatterns = [
    path("testing/", views.testing, name="testing"),
    path("", views.home, name="home"),
    path("products/", views.Products, name="home"),
]