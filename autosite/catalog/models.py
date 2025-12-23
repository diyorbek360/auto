from django.db import models
<<<<<<< HEAD

=======
>>>>>>> 5ca6d7ac49fd4e923175c2b31c65329d161147aa
class Auto(models.Model):
    brand = models.CharField("Марка", max_length=50)
    name = models.CharField("Модель", max_length=100)
    year = models.IntegerField("Год выпуска")
    mileage = models.IntegerField("Пробег (км)")
    price = models.IntegerField("Цена")
    image = models.ImageField("Фото", upload_to='cars/')
    details = models.TextField("Описание", blank=True)

    def __str__(self):
        return f"{self.brand} {self.name}"
<<<<<<< HEAD
=======

>>>>>>> 5ca6d7ac49fd4e923175c2b31c65329d161147aa
