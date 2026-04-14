from django.contrib import admin
from .models import Product, Category

# Регистрация категорий
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

# Регистрация товаров
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'price', 'category', 'created_at')
    list_filter = ('category', 'brand')
    search_fields = ('name', 'brand')