from django.db import models


# Create your models here.

class Auto(models.Model):
    brand = models.CharField(max_length=100,
                             help_text="Введите название бренда",
                             verbose_name="Бренд")
    model = models.CharField(max_length=100,
                             help_text="Введите модель",
                             verbose_name="Модель")
    year = models.IntegerField(help_text="Введите год выпуска", null=True, blank=True)
    color = models.CharField(max_length=50,
                             help_text="Введите цвет автомобиля",
                             verbose_name="Цвет автомобиля")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.color}"

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
