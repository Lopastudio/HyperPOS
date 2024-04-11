from django.contrib import admin
from core.models import Product, CartItem
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy

admin.site.register(Product)
admin.site.register(CartItem)

admin.site.site_header = 'HyperPOS - Administration'