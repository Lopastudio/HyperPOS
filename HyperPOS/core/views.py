from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product

def testing(request):
    return HttpResponse("Hello :)")

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def Products(request):
  myproducts = Product.objects.all().values()
  template = loader.get_template('products.html')
  context = {
    'myproducts': myproducts,
  }
  return HttpResponse(template.render(context, request))