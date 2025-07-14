from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('contacts.html', views.feedback, name='contacts'),
]
