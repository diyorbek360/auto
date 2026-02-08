from django.urls import path
from .views import index_view, catalog_view, product_detail

urlpatterns = [
    path('', index_view, name='index'),
    path('catalog/', catalog_view, name='catalog'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]

