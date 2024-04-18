from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages #mention in presentation
from decimal import Decimal

# Websites:

def testing(request): # Simple testing request (can be used to test the website´s status)
    return HttpResponse("Hello :)") # Return a simple message

def about(request): # About page
    return render(request, "about.html") # Render final page

@login_required
def products_view(request): # Products view page
    try:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        products = Product.objects.all() # Add all products into a list
        return render(request, 'products.html', {'products': products, 'cart_items': cart_items, 'total_price': total_price}) # Render final webpage with products
    except Exception as e:
        return HttpResponse(f"Error occured :(  - {e}") # Simple error fallback


#App logic:

@login_required
def home(request): # Display home page
    try: 
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        products = Product.objects.all()
        return render(request, 'home.html', {'products': products, 'cart_items': cart_items, 'total_price': total_price})
    except Exception as e:
        return HttpResponse(f"Error occured :(  - {e}")

  
def add_to_cart(request, product_id): # Add items to the cart based on product id
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('core:product_list')


def add_product_by_ean(request, ean):# Add items to the cart based on EAN
    try:
        eanisko = int(ean)
    except ValueError:
        return redirect('core:product_list')
    try:
        product = Product.objects.get(ean=eanisko)
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('core:product_list')
    except Product.DoesNotExist:
        return redirect('core:product_list')


def remove_from_cart(request, item_id): # Remove item from the cart based on ID
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('core:product_list')



#Payment system


@login_required
def cash_pay(request, given): # Cash payment (GIVEN MONEY - TOTAL_PRICE = output)
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    given_amount = Decimal(given)
    change_due = given_amount - total_price
    messages.success(request, f'Change Breakdown: {change_due}')
    cart_items.delete()
    return redirect('core:product_list')

@login_required
def card_pay(request): # Card payment
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    messages.success(request, f'Charge: {total_price}')
    cart_items.delete()
    return redirect('core:product_list')

@login_required
def clear_cart(request): # Clear cart
    cart_items = CartItem.objects.filter(user=request.user)
    cart_items.delete()
    #messages.success(request, 'Cart cleared') # Can be enabled, if you want
    return redirect('core:product_list')