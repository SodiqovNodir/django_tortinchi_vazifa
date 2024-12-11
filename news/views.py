from django.shortcuts import render

from .models import Brand,Cars

def brand(request):
    brands = Brand.objects.all()
    return render(request, "brand.html", {'brands' : brands})

def car(request):
    cars = Cars.objects.all()
    return render(request, 'cars.html', {'cars' : cars})