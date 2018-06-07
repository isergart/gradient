# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User
from page.models import Tag
from datetime import datetime
import random
from django.utils.encoding import python_2_unicode_compatible


# Create News model
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок:', help_text='Не более 100 символов (включая пробелы)')
    description = models.CharField('описание:', max_length=2000, blank=False, help_text='SEO поле предназначено для мета-тега description')
    teaser = models.TextField(max_length=200, verbose_name='аннотация:', blank=True, help_text='Не обязательное поле! Заполните краткое описание поста. Не более 200 символов (включая пробелы).<br> Если оставить пустым, то возьмутся первые 200 символов из содержания статьи')
    content = models.TextField(verbose_name='содержание:', blank=True, help_text='Наполнение статьи.')
    slug = models.SlugField('URL:', help_text='человекоподобный URL поста, латинскими буквами')
    publishied = models.BooleanField('публикация', default=False, help_text="Если не указано, страница не будет доступна для просмотра")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', help_text='Время и дата не будет отображаться на сайте!')
    date_publishied = models.DateTimeField(default=datetime.now, verbose_name='дата публикации', help_text='Время публикации поста. Отображается на сайте')
    tag = models.ManyToManyField(Tag, related_name='news_tags', related_query_name='news_tag', verbose_name='метки', help_text='SEO поле предназначено для мета-тегов keywords')
    social_button = models.BooleanField(default=True, verbose_name='разрешить перепост', help_text='Добавить кнопку: "Поделиться" в Facebok, Twitter, Вконтакт, Одноклассники, Мой мир.<br> Для перепоста на свою страницу')
    user = models.ForeignKey(User, verbose_name='автор поста', on_delete=models.CASCADE,)  # editable=False, default=False
    image = models.ForeignKey('Image', related_name='news_images', blank=True, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'news_post'
        verbose_name = 'новость'
        verbose_name_plural = 'новость'
        ordering = ['-date_created']

    def __str__(self):
        return '%s' % self.title

    def save(self, **kwargs):
        if not self.image:
            self.image = Image.objects.get(id=1)
        else:
            number = random.randint(1, 6)
            self.image = 'news/random/pic' + str(number) + '.jpg'
        super(Post, self).save()


# Create Image for News model
@python_2_unicode_compatible
class Image(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок:', blank=True, help_text='Не обязательное поле!')
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/',verbose_name='изображение', blank=True, help_text='Размер изображения не более 1Mб. Горизонтального вида')
    watermark = models.BooleanField(default=0, verbose_name='защита', help_text='Добавляется водяной знак на фотографию')  # blank=True
    news = models.ForeignKey(Post, related_name='news_image', verbose_name='галерея', on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = 'news_image'
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
        ordering = ['id']

    def __str__(self):
        return '%s' % self.name
