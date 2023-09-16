from django.db import models

from blog.apps import BlogConfig


app_name = BlogConfig.name

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='blog_imgs/', **NULLABLE, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    publication_date = models.DateField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.title}, {self.views}, {self.publication_date}'

    class Meta:
        verbose_name = 'публикации'
        verbose_name_plural = 'публикации'
        ordering = 'title',  'views', 'publication_date'
