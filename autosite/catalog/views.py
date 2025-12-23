<<<<<<< HEAD
from django.shortcuts import render
from .models import Auto

def index_view(request):
    cars = Auto.objects.all()  # все авто для главной
    return render(request, 'catalog/index.html', {
        'cars': cars
    })

def catalog_view(request):
    cars = Auto.objects.all()  # все авто для каталога
    return render(request, 'catalog/catalog.html', {
        'cars': cars
    })
=======
from .models import Auto
from django.shortcuts import render

def index_view(request):
    return render(request, 'catalog/index.html')

def catalog_view(request):
    return render(request, 'catalog/catalog.html')


>>>>>>> 5ca6d7ac49fd4e923175c2b31c65329d161147aa
