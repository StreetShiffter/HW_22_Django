from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy

from blog.models import BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    fields = '__all__'
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:list')


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        bl_obj = super().get_object(queryset)
        bl_obj.views_count += 1
        bl_obj.save(update_fields=['views_count'])
        return bl_obj


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'posts'
    paginate_by = 5  # Опционально: пагинация

    def get_queryset(self):
        # Только опубликованные посты
        return BlogPost.objects.filter(is_published=True)


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:list')