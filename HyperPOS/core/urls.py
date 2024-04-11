from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),
]
