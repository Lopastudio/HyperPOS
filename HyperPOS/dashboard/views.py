from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from core.models import Product


def dashboard(request):
    return render(request, 'dashboard.html', {})

def fm(request):
    return render(request, 'dashboard_flexmonster.html', {})

def pivot_data(request):
    dataset = Product.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)