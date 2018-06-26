# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Vacancy(models.Model):
    """
    Create Vacancy model
    """
    vacancy = models.CharField(_('вакансия:'), max_length=30, blank=True, help_text=_('Предлагаемая должность'))
    description = models.TextField(_('требования:'), max_length=200, blank=False, help_text=_('Требование к кандидату'))
    added_date = models.DateField(_('дата добавления:'), null=True, blank=True)
    show = models.BooleanField(_('отображать'), default=False, help_text=_('Отображать вакансию на сайте'))

    class Meta:
        db_table = 'documents_vacancy'
        verbose_name = _('вакансию')
        verbose_name_plural = _('вакансия')
        ordering = ('added_date',)

    def __str__(self):
        return '%s' % self.vacancy


@python_2_unicode_compatible
class Partner(models.Model):
    """
    Create Partner model
    """
    name = models.CharField(_('организация:'), max_length=30, blank=False, help_text=_('Название организации. Пример: ООО "Ромашка"'))
    url = models.URLField(_('URL:'), max_length=30, blank=True, help_text=_('URL сайта организации'))
    location = models.CharField(_('адрес:'), max_length=30, blank=True)
    phone = models.CharField(_('телефон:'), max_length=30, blank=True)
    fax = models.CharField(_('факс:'), max_length=30, blank=True)
    logo = models.ImageField(_('логотип'), upload_to='partner', max_length=100, blank=False, help_text=_('Размер не более 1Mб'))
    show = models.BooleanField(_('отображать'), default=False, help_text=_('Отображать на главной'))

    class Meta:
        db_table = 'documents_partner'
        verbose_name = _('партнера')
        verbose_name_plural = _('партнер')
        ordering = ('name',)

    def __str__(self):
        return '%s' % self.name


@python_2_unicode_compatible
class Block(models.Model):
    """
    Create Block model
    """
    CATEGORY_CHOICES = (
        ('1', _('Промышленное холодоснабжение')),
        ('2', _('Внутренние инженерные системы')),
        ('3', _('Фруктохранилище')),
        ('4', _('Овощехранилище')),
        ('5', _('Cправочная информация')),
        ('6', _('Cправочная информация')),
        ('7', _('Сертификаты')),
        ('8', _('Свидетельства')),
        ('9', _('Отзывы')),
        ('10', _('Письма')),
        )
    title = models.CharField(max_length=100, verbose_name=_('заголовок:'), help_text=_('Не более 100 символов (включая пробелы)'))
    description = models.CharField(_('описание:'), max_length=200, blank=False, help_text=_('SEO поле предназначено для мета-тега description'))
    teaser = models.CharField(max_length=200, verbose_name=_('аннотация:'), blank=True, help_text=_('Не обязательное поле! Заполните краткое описание поста. Не более 200 символов (включая пробелы).<br> Если оставить пустым, то возьмутся первые 200 символов из содержания статьи'))
    content = models.TextField(verbose_name=_('содержание:'), blank=True, help_text=_('Наполнение статьи.'))
    image_button = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name=_('иконка'), blank=True, help_text=_('Размер изображения не более 1Mб. Горизонтального вида'))
    show_button = models.BooleanField(_('отображать'), default=False, help_text=_('Если отмечено, страница будет показана в главном меню'))
    image = models.ForeignKey('Image', verbose_name=_('изображение:'), related_name='block_images', on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(_('категория:'), max_length=1, choices=CATEGORY_CHOICES, default='1')

    class Meta:
        db_table = 'documents_block'
        verbose_name = _('блок')
        verbose_name_plural = _('блок')
        ordering = ('id',)

    def __str__(self):
        return '%s' % self.id


@python_2_unicode_compatible
class Image(models.Model):
    """
    Create Image for Block model
    """
    title = models.CharField(_('заголовок:'), max_length=50, blank=True, help_text=_('Не обязательное поле!'))
    description = models.CharField(_('описание:'), max_length=2000, blank=False, help_text=_('SEO поле предназначено для мета-тега description'))
    image = models.ImageField(_('изображение'), upload_to='uploads/%Y/%m/%d/', blank=True, help_text=_('Размер изображения не более 1Mб. Горизонтального вида'))
    watermark = models.BooleanField(_('защита'), default=0, help_text=_('Добавляется водяной знак на фотографию'))
    block = models.ForeignKey(Block, related_name='block_image', verbose_name=_('галерея'), on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = 'documents_image'
        verbose_name = _('изображение')
        verbose_name_plural = _('изображения')
        ordering = ['id']

    def __str__(self):
        return '%s' % self.title
