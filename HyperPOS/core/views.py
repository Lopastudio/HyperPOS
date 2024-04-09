from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from django.http import HttpResponse
from django.template import loader
from .models import Product
from decimal import Decimal

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
    if request.method == 'POST':
        product = Product.objects.get(ean=product_id)
        cart = request.session.get('cart', [])
        cart.append({
            'name': product.name,
            'price': float(product.price),
        })
        request.session['cart'] = cart
        messages.success(request, f"{product.name} added to cart.")
        return redirect('cart_view')
    else:
        return redirect('product_list')  # Redirect to product list view
