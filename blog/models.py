from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(max_length = 300, verbose_name='Описание')
    preview = models.ImageField(upload_to='images_blog/', verbose_name='Превью', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0,verbose_name="Количество просмотров")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
