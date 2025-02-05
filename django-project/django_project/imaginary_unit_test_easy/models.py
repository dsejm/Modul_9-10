from django.db import models

# Create your models here.

class ImaginaryObject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название объекта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Воображаемый объект"
        verbose_name_plural = "Воображаемые объекты"