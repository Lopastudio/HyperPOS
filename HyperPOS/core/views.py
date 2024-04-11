from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse
from django.template import loader
from .models import Product

def testing(request):
    return HttpResponse("Hello :)")

def home(request):
    products = Product.objects.all()
    context = {'myproducts': products}
    return render(request, 'home.html', context)

def Products(request):
    products = Product.objects.all().values()
    template = loader.get_template('products.html')
    context = {
      'myproducts': products,
    }
    return HttpResponse(template.render(context, request))

def atc(request, product_id):
    # add to cart shit fuck doesnt work :(((


def atc_search(request):
    if request.method == 'POST':
        ean = request.POST.get('ean_search', None)
        if ean:
            try:
                product = Product.objects.get(ean=ean)
                return HttpResponse(f"The product name is: {product.name}")
            except Product.DoesNotExist:
                return HttpResponse("Product not found.")
    return HttpResponse("Invalid request.")
    