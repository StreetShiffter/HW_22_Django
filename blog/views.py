from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse, reverse_lazy

from blog.models import BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    # fields = '__all__' # спец метод для добавления всех полей разом
    fields = ['title', 'content', 'preview',]
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        form.instance.is_published = True  # ← принудительно публикуем
        return super().form_valid(form)



class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.object.pk})


class BlogDetailView(DetailView):
    model = BlogPost
    context_object_name = 'post'

    def get_object(self, queryset=None):
        bl_obj = super().get_object(queryset)
        bl_obj.views_count += 1
        bl_obj.save(update_fields=['views_count'])
        return bl_obj


class BlogListView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    paginate_by = 4  # Опционально: пагинация по 4 элемента

    def get_queryset(self):
        # Только опубликованные посты
        return BlogPost.objects.filter(is_published=True)


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:list')