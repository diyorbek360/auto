from django.contrib import admin
from .models import Auto

class AutoAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('brand', 'name', 'year', 'price')
=======
    list_display = ('name', 'price', 'image')  # только существующие поля
>>>>>>> 5ca6d7ac49fd4e923175c2b31c65329d161147aa

admin.site.register(Auto, AutoAdmin)
