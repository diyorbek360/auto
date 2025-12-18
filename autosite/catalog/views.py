from django.shortcuts import render
from .models import Auto

def catalog_view(request):
    autos = Auto.objects.all()  
    return render(request, "catalog/index.html", {"autos": autos})


