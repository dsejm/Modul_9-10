from django.test import TestCase
from imaginary_unit_test_middle.models import Category, Product
from imaginary_unit_test_middle.factories import CategoryFactory, ProductFactory

# Create your tests here.

class CategoryModelTest(TestCase):
    fixtures = ['categories.json']  # Загружаем фикстуру

    def test_category_creation(self):
        # Проверяем, что категории загружены из фикстуры
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, "Электроника")
        self.assertEqual(category.description, "Техника и гаджеты")


class ProductModelTest(TestCase):
    def test_product_creation(self):
        # Создаем объект Product с помощью фабрики
        product = ProductFactory()

        # Проверяем, что объект был создан
        self.assertEqual(Product.objects.count(), 1)

        # Проверяем, что поля заполнены корректно
        self.assertIsNotNone(product.name)
        self.assertIsNotNone(product.price)
        self.assertIsNotNone(product.category)
        self.assertIsNotNone(product.stock)

    def test_product_with_specific_category(self):
        # Создаем категорию вручную
        category = CategoryFactory(name="Тестовая категория")

        # Создаем продукт с указанной категорией
        product = ProductFactory(category=category)

        # Проверяем, что категория продукта совпадает с созданной
        self.assertEqual(product.category.name, "Тестовая категория")
