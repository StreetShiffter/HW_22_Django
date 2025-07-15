from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'), # главная страницая
    path('contacts/', views.feedback, name="{%url'catalog: contacts/'%}"),  # корректное имя
]