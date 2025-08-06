from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, DetailView
from django.views import View


from catalog.models import Products, Category

class HomeListView(ListView):
    '''Главная страница'''
    model = Products
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        '''Метод распаковки моделей'''
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        context['category'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    '''Загрузка страницы с конкретным продуктом по первичному ключу'''
    model = Products
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        '''Метод распаковки моделей'''
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        context['category'] = Category.objects.all()
        return context


class FeedbackView(View):
    template_name = 'catalog/contacts.html'# Нужно прописать genm, т.к. нету действия view.

    def get(self, request):
        # При GET-запросе просто показываем шаблон
        return render(request, self.template_name)

    def post(self, request):
        # При POST — забираем данные вручную
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Обрабатываем и отвечаем
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


