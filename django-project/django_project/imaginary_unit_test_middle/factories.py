import factory
from imaginary_unit_test_middle.models import Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")
    description = factory.Faker("text")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)
    stock = factory.Faker("random_int", min=0, max=100)