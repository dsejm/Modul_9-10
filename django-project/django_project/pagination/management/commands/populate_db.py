# populate_db.py
from django.core.management.base import BaseCommand
from faker import Faker
from pagination.models import Product, Review

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными: 30 продуктов и 1-2 отзыва на каждый.'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Создаем 30 продуктов
        for _ in range(30):
            product = Product.objects.create(
                name=fake.catch_phrase(),
                description=fake.text(max_nb_chars=200)
            )

            # Создаем 1-2 отзыва для каждого продукта
            for _ in range(fake.random_int(min=1, max=2)):
                Review.objects.create(
                    product=product,
                    author=fake.name(),
                    text=fake.paragraph(nb_sentences=3)
                )

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными!'))