from django.urls import path
from .views import (
    index_view,
    catalog_view,
    product_detail,
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    path('', index_view, name='home'),
    path('catalog/', catalog_view, name='catalog'),
    path('product/<int:pk>/', product_detail, name='product_detail'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]