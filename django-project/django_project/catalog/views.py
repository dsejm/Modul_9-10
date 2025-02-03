from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.

def product_list(request):
    # Извлекаем все категории и продукты, у которых stock > 0
    categories = Category.objects.all()
    products = Product.objects.filter(stock__gt=0)  # Фильтруем продукты

    # Передаем данные в шаблон
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, id):
    # Извлекаем продукт по id или возвращаем 404, если продукт не найден
    product = get_object_or_404(Product, id=id)

    # Передаем данные в шаблон
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)