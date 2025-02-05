from django.test import TestCase
from imaginary_unit_test_easy.models import ImaginaryObject


# Create your tests here.

class ImaginaryObjectModelTest(TestCase):
    def test_create_imaginary_object(self):
        # Создаем объект модели
        obj = ImaginaryObject.objects.create(name="Тестовый объект")

        # Проверяем, что объект был создан
        self.assertEqual(ImaginaryObject.objects.count(), 1)

        # Проверяем, что поле name заполнено корректно
        self.assertEqual(obj.name, "Тестовый объект")

        # Проверяем строковое представление объекта
        self.assertEqual(str(obj), "Тестовый объект")