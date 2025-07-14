from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

# def contacts(request):
#     return render(request, 'contacts.html') # ДЛЯ ПРОСТОГО ОТОБРАЖЕНИЯ

def feedback(request):# УНИВЕРСАЛЬНАЯ ФУНКЦИЯ ОТОБРАЖЕНИЯ И ОТПРАВКИ ФОРМЫ
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


