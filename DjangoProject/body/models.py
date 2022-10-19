from django.db import models
from django.urls import reverse_lazy


class Task(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    task = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата редактирования', auto_now=True)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', default='No photo')
    is_published = models.BooleanField('Состояние', default=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name='Категoрия', )
    views = models.IntegerField('Просмотры: ', default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('home')  # 'task', kwargs={'pk': self.pk}

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']


class Categories(models.Model):
    title = models.CharField('Название категории', max_length=150, db_index=True)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
