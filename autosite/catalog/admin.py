from django.contrib import admin
from .models import Auto

class AutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # только существующие поля

admin.site.register(Auto, AutoAdmin)
