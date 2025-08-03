from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Products, Category


def home(request):
    '''Загрузка стартовой страницы'''
    products = Products.objects.all()
    category = Category.objects.all()
    context = {'products': products, 'category': category}
    return render(request, 'home.html', context = context)

def product(request, pk):
    '''Загрузка страницы с конкретным продуктом по первичному ключу'''
    # products = Products.objects.get(pk=pk) - простой способ
    product = get_object_or_404(Products, pk=pk)
    category = product.category

    print(f"Product ID: {product.pk}")
    print(f"Product name: '{product.name}'")
    print(f"Name length: {len(product.name)}")
    print(f"Name repr: {repr(product.name)}")

    context = {'product': product, 'category': category}
    return render(request, 'product.html', context = context)


def feedback(request):
    '''УНИВЕРСАЛЬНАЯ ФУНКЦИЯ ОТОБРАЖЕНИЯ И ОТПРАВКИ ФОРМЫ'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


