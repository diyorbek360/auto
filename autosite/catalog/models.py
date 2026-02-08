from django.db import models

class Category(models.Model):
    name = models.CharField("Категория", max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.CharField("Бренд", max_length=100)
    name = models.CharField("Название", max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    price = models.PositiveIntegerField("Цена")
    image = models.ImageField("Фото", upload_to='products/')
    tag = models.CharField("Метка", max_length=20, blank=True)  # Trend / New / Sale
    description = models.TextField("Описание", blank=True)
    
    # Новые поля для телефона
    screen = models.CharField("Экран", max_length=100, blank=True)
    cpu = models.CharField("Процессор", max_length=100, blank=True)
    ram = models.CharField("RAM", max_length=50, blank=True)
    storage = models.CharField("Память", max_length=50, blank=True)
    camera = models.CharField("Камера", max_length=100, blank=True)
    battery = models.CharField("Батарея", max_length=50, blank=True)
    sim = models.CharField("SIM / Сети", max_length=50, blank=True)
    color = models.CharField("Цвет", max_length=50, blank=True)
    warranty = models.CharField("Гарантия", max_length=50, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.name}"