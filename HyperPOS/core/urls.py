from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:product_id>/', views.atc, name='atc'), # type: ignore
    path('search/', views.atc_search, name='searching'),
    path("testing/", views.testing, name="testing"),
    path('', views.home, name='home'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),
    path("products/", views.Products, name="home"),
]
