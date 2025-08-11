from django.urls import path
from catalog.apps import CatalogConfig
from .views import HomeListView, ProductDetailView, FeedbackView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product"),
    path('contacts/',FeedbackView.as_view(), name="contacts"),
    path('', HomeListView.as_view(), name="home"),
    path('product/create/', ProductCreateView.as_view(), name="create"),
]