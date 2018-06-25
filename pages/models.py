# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Tag(models.Model):
    """
    Create Tag model
    """
    name = models.CharField(max_length=50, verbose_name='имя метки', help_text='Укажите ключевое слово(мета тег)')
    slug = models.SlugField('URL', help_text='укажите на латинице', unique=True)
    cloud = models.BooleanField(verbose_name='отображать', default=False, help_text='Если указано, метка видна в облаке тегов.')

    class Meta:
        db_table = 'pages_tag'
        verbose_name = 'тег'
        verbose_name_plural = 'ключевые слова'
        ordering = ['name']

    def __str__(self):
        return '%s' % self.name


@python_2_unicode_compatible
class Carousel(models.Model):
    """
    Create Carousel model
    """
    title = models.CharField(max_length=50, verbose_name='заголовок:', blank=False, help_text='Не обязательное поле!')
    description = models.CharField('описание:', max_length=2000, blank=False, help_text='развернутое описание заголовка')
    image = models.ImageField(upload_to='carousel', max_length=100, blank=True, verbose_name='изображение', help_text='Размер не более 1Mб. Горизонтального вида')
    show = models.BooleanField('отображать', default=True, help_text='Если отмечено, слайд будет показана в карусели')
    watermark = models.BooleanField('маска', default=False, help_text='Наложить маску на изображение')  # blank=True
    order = models.PositiveIntegerField('сортировка', blank=True, default=0, help_text='Укажите в каком порядке сортируется слайд.')
    link = models.CharField('URL кнопки', max_length=200, blank=True, help_text='Если не указано, кнопка не отображается. Укажите URL адрес для кнопки. Пример: "/about/clients/"')

    class Meta:
        db_table = 'pages_carousel'
        verbose_name = 'слайд'
        verbose_name_plural = 'карусель'
        ordering = ('order',)

    def __str__(self):
        return '%s' % self.title


@python_2_unicode_compatible
class Chank(models.Model):
    """
    Create Chank model
    """
    title = models.CharField(max_length=50, verbose_name='название:', blank=False, help_text='Не обязательное поле!')
    label = models.CharField(max_length=50, verbose_name='идентификатор:', blank=False, help_text='Метка чанка!')
    code = models.TextField('код:', max_length=2000, blank=False, help_text='Код сниппета')
    show = models.BooleanField('активировать', default=False, help_text="Если отмечено, чанк начнет работать")

    class Meta:
        db_table = 'pages_chank'
        verbose_name = 'чанк'
        verbose_name_plural = 'чанк'
        ordering = ('title',)

    def __str__(self):
        return '%s' % self.title


@python_2_unicode_compatible
class Page(FlatPage):
    """
    Redefine old FlatPage model
    """
    description = models.CharField('описание', max_length=200, blank=False, help_text='SEO поле предназначено для мета-тега description')
    block = models.TextField(verbose_name='дополнительное поле', blank=True, help_text='Если указано, появится  выделенный блок текста')
    tag = models.ManyToManyField(Tag, related_name='tags', related_query_name='tag', verbose_name='метки', help_text='SEO поле предназначено для мета-тегов keywords')
    publishied = models.BooleanField('публикация', default=False, help_text='Если не указано, страница не будет доступна для просмотра')
    show = models.BooleanField('отображать', default=False, help_text='Если отмечено, страница будет показана в главном меню')
    order = models.PositiveIntegerField('сортировка', default=0, help_text='Укажите в каком порядке сортируется меню. Значение меньше - выше/левее, больше - ниже/правее')
    parent = models.CharField('URL родителя', max_length=20, blank=True, help_text='Пример: /about/clients/. Здесь родителем является /about/. Убедитесь, что есть начальные и конечные слэши.')

    class Meta:
        db_table = 'pages_page'
        verbose_name = 'страницу'
        verbose_name_plural = 'страница'
        ordering = ('order',)

    def __str__(self):
        return "%s -- %s" % (self.url, self.parent)
