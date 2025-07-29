from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Products, Category


def home(request):
    '''Загрузка стартовой страницы'''
    products = Products.objects.all()
    category = Category.objects.all()
    context = {'products': products, 'category': category}
    return render(request, 'home.html', context = context)


def feedback(request):
    '''УНИВЕРСАЛЬНАЯ ФУНКЦИЯ ОТОБРАЖЕНИЯ И ОТПРАВКИ ФОРМЫ'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


