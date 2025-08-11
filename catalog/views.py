from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse, reverse_lazy

from catalog.forms import ProductsForm
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


class ProductCreateView(CreateView):
    model = Products
    form_class = ProductsForm
    # fields = '__all__' # спец метод для добавления всех полей разом
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:products_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:products_list')


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


