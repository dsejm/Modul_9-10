import os
import django
from faker import Faker
from datetime import datetime, timedelta

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from imaginary_unit_test_hard.models import Author, Book

fake = Faker()

def create_authors(num_authors=10):
    """Создает авторов."""
    for _ in range(num_authors):
        Author.objects.create(
            name=fake.name(),
            bio=fake.text()
        )

def create_books(num_books=20):
    """Создает книги и связывает их с авторами."""
    authors = list(Author.objects.all())
    for _ in range(num_books):
        book = Book.objects.create(
            title=fake.sentence(nb_words=4),
            publication_date=fake.date_between(start_date='-30y', end_date='today'),
            pages=fake.random_int(min=100, max=500)
        )
        # Связываем книгу с 1-3 случайными авторами
        book.authors.set(fake.random_elements(elements=authors, length=fake.random_int(min=1, max=3)))

if __name__ == "__main__":
    print("Создание авторов...")
    create_authors()

    print("Создание книг...")
    create_books()

    print("База данных успешно заполнена!")