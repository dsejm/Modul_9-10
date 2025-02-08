from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name="Продукт")
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Отзыв от {self.author} на {self.product.name}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
