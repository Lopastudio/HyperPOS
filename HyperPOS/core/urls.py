from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('atc/<int:product_id>/', views.atc, name='atc'),
    path('cart/', views.atc, name='cart_view'),
    path("testing/", views.testing, name="testing"),
    path('', views.home, name='home'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),
    path("products/", views.Products, name="home"),
]
