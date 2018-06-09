# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create Vacancy model
@python_2_unicode_compatible
class Vacancy(models.Model):
    vacancy = models.CharField('вакансия:',max_length=30, blank=True, help_text='Предлагаемая должность')
    description = models.TextField('требования:', max_length=200, blank=False, help_text='Требование к кандидату')
    added_date = models.DateField('дата добавления:',null=True, blank=True)
    show = models.BooleanField('отображать', default=False, help_text='Отображать вакансию на сайте')

    class Meta:
        db_table = 'documents_vacancy'
        verbose_name = 'вакансию'
        verbose_name_plural = 'вакансия'
        ordering = ('added_date',)

    def __str__(self):
        return '%s' % self.vacancy

# Create Partner model
@python_2_unicode_compatible
class Partner(models.Model):
    name = models.CharField('партнер:',max_length=30, blank=False, help_text='Название организации')
    url = models.URLField('URL:',max_length=30, blank=True, help_text='URL сайта организации')
    location = models.CharField('адрес:',max_length=30, blank=True)
    phone = models.CharField('телефон:',max_length=30, blank=True)
    fax = models.CharField('факс:',max_length=30, blank=True)
    logo = models.ImageField('логотип', upload_to = 'partner', max_length=100, blank=False, help_text='Размер не более 1Mб')
    show = models.BooleanField('отображать', default=False, help_text='Отображать партнера на сайте')

    class Meta:
        db_table = 'documents_partner'
        verbose_name = 'партнера'
        verbose_name_plural = 'партнер'
        ordering = ('name',)

    def __str__(self):
        return '%s' % self.name


# Create Block model
@python_2_unicode_compatible
class Block(models.Model):
    CATEGORY_CHOICES = (
        ('a', 'Промышленное холодоснабжение'),
        ('b', 'Внутренние инженерные системы'),
        ('c', 'Фруктохранилище'),
        ('d', 'Овощехранилище'),
        ('e', 'Cправочная информация'),
        ('f', 'Cервисное обслуживание'),
        ('g', 'Сертификаты'),
        ('h', 'Свидетельства'),
        ('i', 'Отзывы'),
        ('j', 'Письма'),
    )
    title = models.CharField(max_length=100, verbose_name='заголовок:', help_text='Не более 100 символов (включая пробелы)')
    description = models.CharField('описание:', max_length=2000, blank=False, help_text='SEO поле предназначено для мета-тега description')
    teaser = models.TextField(max_length=200, verbose_name='аннотация:', blank=True, help_text='Не обязательное поле! Заполните краткое описание поста. Не более 200 символов (включая пробелы).<br> Если оставить пустым, то возьмутся первые 200 символов из содержания статьи')
    content = models.TextField(verbose_name='содержание:', blank=True, help_text='Наполнение статьи.')
    image_button = models.ImageField(upload_to='uploads/%Y/%m/%d/',verbose_name='изображение', blank=True, help_text='Размер изображения не более 1Mб. Горизонтального вида')
    show_button = models.BooleanField('отображать', default=False, help_text='Если отмечено, страница будет показана в главном меню')
    image = models.ForeignKey('Image', related_name='block_images', on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField('тип блока:', max_length=1, choices=CATEGORY_CHOICES, default='a')

    class Meta:
        db_table = 'documents_block'
        verbose_name = 'блок'
        verbose_name_plural = 'документ'
        ordering = ('id',)

    def __str__(self):
        return '%s' % self.id


# Create Image for Block model
@python_2_unicode_compatible
class Image(models.Model):
    title = models.CharField('заголовок:', max_length=50, blank=True, help_text='Не обязательное поле!')
    description = models.CharField('описание:', max_length=2000, blank=False, help_text='SEO поле предназначено для мета-тега description')
    image = models.ImageField('изображение', upload_to='uploads/%Y/%m/%d/', blank=True, help_text='Размер изображения не более 1Mб. Горизонтального вида')
    watermark = models.BooleanField('защита', default=0, help_text='Добавляется водяной знак на фотографию')
    block = models.ForeignKey(Block, related_name='block_image', verbose_name='галерея', on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = 'documents_image'
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
        ordering = ['id']

    def __str__(self):
        return '%s' % self.title
