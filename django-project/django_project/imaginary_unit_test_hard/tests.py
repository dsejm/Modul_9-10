from django.test import TestCase
from imaginary_unit_test_hard.models import Author, Book
from datetime import date


# Create your tests here.

class AuthorModelTest(TestCase):
    def test_author_creation(self):
        # Создаем автора
        author = Author.objects.create(name="Тестовый автор", bio="Тестовая биография")

        # Проверяем, что объект был создан
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(author.name, "Тестовый автор")
        self.assertEqual(author.bio, "Тестовая биография")


class BookModelTest(TestCase):
    def test_book_creation(self):
        # Создаем авторов
        author1 = Author.objects.create(name="Автор 1", bio="Биография 1")
        author2 = Author.objects.create(name="Автор 2", bio="Биография 2")

        # Создаем книгу
        book = Book.objects.create(
            title="Тестовая книга",
            publication_date=date.today(),
            pages=200
        )
        book.authors.set([author1, author2])

        # Проверяем, что объект был создан
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(book.title, "Тестовая книга")
        self.assertEqual(book.pages, 200)
        self.assertEqual(book.authors.count(), 2)

    def test_book_with_specific_authors(self):
        # Создаем авторов
        author1 = Author.objects.create(name="Автор 1", bio="Биография 1")
        author2 = Author.objects.create(name="Автор 2", bio="Биография 2")

        # Создаем книгу с указанными авторами
        book = Book.objects.create(
            title="Тестовая книга",
            publication_date=date.today(),
            pages=200
        )
        book.authors.set([author1, author2])

        # Проверяем, что авторы книги совпадают с созданными
        self.assertEqual(book.authors.first().name, "Автор 1")
        self.assertEqual(book.authors.last().name, "Автор 2")
