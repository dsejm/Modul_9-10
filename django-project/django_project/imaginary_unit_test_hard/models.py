from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя автора")
    bio = models.TextField(verbose_name="Биография", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    authors = models.ManyToManyField(Author, related_name="books", verbose_name="Авторы")
    publication_date = models.DateField(verbose_name="Дата публикации")
    pages = models.IntegerField(verbose_name="Количество страниц")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
