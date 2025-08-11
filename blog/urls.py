# blog/urls.py
from django.urls import path
from .views import BlogCreateView, BlogDetailView, BlogListView, BlogUpdateView, BlogDeleteView
from .apps import BlogConfig

app_name = BlogConfig.name  # или просто 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),           # /blog/
    path('create/', BlogCreateView.as_view(), name='create'), # /blog/create/
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),  # /blog/1/
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='update'),  # /blog/1/edit/
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),  # /blog/1/delete/
]