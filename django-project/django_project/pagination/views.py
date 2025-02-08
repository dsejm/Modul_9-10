from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import ContactForm, ReviewForm
from .models import Item, Product, Review, Contact

# Create your views here.

def item_list(request):
    # Получаем все объекты модели Item
    items = Item.objects.all()

    # Создаем пагинатор с 5 объектами на странице
    paginator = Paginator(items, 5)
    page_number = request.GET.get('page')  # Получаем номер страницы из запроса
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы

    # Передаем объект страницы в шаблон
    return render(request, 'pagination/item_list.html', {'page_obj': page_obj})

def contact_view(request):
    if request.method == 'POST':
        # Если данные отправлены через POST, создаем форму с этими данными
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохраняем данные в базу данных
            form.save()
            # Перенаправляем пользователя на страницу с сообщением об успехе
            return redirect('contact_success')
    else:
        # Если запрос GET, создаем пустую форму
        form = ContactForm()

    # Передаем форму в шаблон
    return render(request, 'pagination/contact_form.html', {'form': form})

def contact_success_view(request):
    # Отображаем страницу с сообщением об успешной отправке
    return render(request, 'pagination/contact_success.html')

# views.py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Review
from .forms import ReviewForm

# views.py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Review
from .forms import ReviewForm

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)  # Пагинация по 10 продуктов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            product_id = request.POST.get('product_id')
            review.product = Product.objects.get(id=product_id)
            review.save()
            return redirect('review_success')  # Перенаправляем на страницу успеха
    else:
        form = ReviewForm()

    return render(request, 'pagination/product_list.html', {
        'page_obj': page_obj,
        'form': form,
    })

def review_success_view(request):
    return render(request, 'pagination/review_success.html')
