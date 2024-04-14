from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
from django.urls import path, re_path
from . import views
from decimal import Decimal


app_name = 'core'

urlpatterns = [
    # Web addresses
    path('', views.home, name='product_list'), #Main homepage
    path('products/', views.products_view, name='products_view'), # Products list page
    path('about/', views.about, name='about_page'), # About page
    
    # Functions: 
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'), # Adding items using list
    path('adde/<ean>/', views.add_product_by_ean, name='add_product_by_ean'), # Adding items using EAN
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'), # Removing items from the cart
    
    re_path(r'^f/cash/(?P<given>\d+\.\d+)/$', views.cash_pay, name='cash_pay'),
    path('f/card/',views.card_pay,name="card_pay"),
    path('f/cc/',views.clear_cart,name="clear_cart"),
    
    # Perma-Links
    #path('/favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))), # no longer used
    
    # MISC / Other
    path('test/', views.testing), # Test, if the website is live ; Can be disabled in final deploynment!
]