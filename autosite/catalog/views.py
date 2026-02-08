from django.shortcuts import render, get_object_or_404
from .models import Product, Category # Проверь, что Category импортирован
from django.db.models import Min, Max, Q


def index_view(request):
    products = Product.objects.all()[:6]
    categories = Category.objects.all()

    print("CATEGORIES:", categories)  # 👈 ВАЖНО

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog/index.html', context)

def catalog_view(request):
    
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(brand__icontains=query)
        )

    # Остальная фильтрация по цене, RAM, storage, color...

    # Берём динамический диапазон цены
    price_range = products.aggregate(
        price_min=Min('price'),
        price_max=Max('price')
    )
    price_min = price_range['price_min'] or 0
    price_max = price_range['price_max'] or 100000

    # Берём выбранные значения из GET
    min_price = int(request.GET.get('min_price', price_min))
    max_price = int(request.GET.get('max_price', price_max))

    # Фильтруем товары по цене
    products = products.filter(price__gte=min_price, price__lte=max_price)

    # Чекбоксы (бренд, RAM, цвет и т.д.)
    brands = Product.objects.values_list('brand', flat=True).distinct()
    rams = Product.objects.values_list('ram', flat=True).distinct()
    storages = Product.objects.values_list('storage', flat=True).distinct()
    colors = Product.objects.values_list('color', flat=True).distinct()

    selected_brands = request.GET.getlist('brand')
    selected_rams = request.GET.getlist('ram')
    selected_storages = request.GET.getlist('storage')
    selected_colors = request.GET.getlist('color')

    # Дополнительная фильтрация по чекбоксам
    if selected_brands:
        products = products.filter(brand__in=selected_brands)
    if selected_rams:
        products = products.filter(ram__in=selected_rams)
    if selected_storages:
        products = products.filter(storage__in=selected_storages)
    if selected_colors:
        products = products.filter(color__in=selected_colors)
    translations = {
    "profile": {"ru": "Профиль", "uz": "Profil", "en": "Profile"},
    "cart": {"ru": "Корзина", "uz": "Savat", "en": "Cart"},
    }
    context = {
        'products': products,
        'price_min': price_min,
        'price_max': price_max,
        'min_price': min_price,
        'max_price': max_price,
        'brands': brands,
        'rams': rams,
        'storages': storages,
        'colors': colors,
        'selected_brands': selected_brands,
        'selected_rams': selected_rams,
        'selected_storages': selected_storages,
        'selected_colors': selected_colors,
        "lang": "ru", 
        "t": translations,
    }
    return render(request, 'catalog/catalog.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product.html', {'product': product})
