from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=50, default='Новая статья')
    anons = models.CharField('Анонс', max_length=250, default='Анонс')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'Новость'
    #     verbose_name_popular = 'Новости'

