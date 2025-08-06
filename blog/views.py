from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View

class BlogCreateView(CreateView):
    pass

class BlogUpdateView(UpdateView):
    pass

class BlogDetailView(DetailView):
    pass

class BlogListView(ListView):
    pass

class BlogDeleteView(DeleteView):
    pass