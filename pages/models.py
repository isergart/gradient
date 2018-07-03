# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Tag(models.Model):
    """Create tag model"""
    name = models.CharField(max_length=50, verbose_name=_('имя'), help_text=_('Укажите ключевое слово(мета тег)'))
    slug = models.SlugField(_('URL'), help_text=_('укажите на латинице'), unique=True)
    cloud = models.BooleanField(verbose_name=_('показывать'), default=False, help_text=_('Если указано, метка видна в облаке тегов.'))

    class Meta:
        db_table = 'pages_tag'
        verbose_name = _('тег')
        verbose_name_plural = _('теги')
        ordering = ['name']

    def __str__(self):
        return '%s' % self.name


@python_2_unicode_compatible
class Carousel(models.Model):
    """Create carousel model"""
    title = models.CharField(max_length=50, verbose_name=_('заголовок:'), blank=False, help_text=_('Не обязательное поле!'))
    description = models.CharField(_('описание:'), max_length=2000, blank=False, help_text=_('развернутое описание заголовка'))
    image = models.ImageField(upload_to='carousel', max_length=100, blank=True, verbose_name=_('изображение'), help_text=_('Размер не более 1Mб. Горизонтального вида'))
    show = models.BooleanField(_('отображать'), default=True, help_text='Если отмечено, слайд будет показана в карусели')
    watermark = models.BooleanField(_('маска'), default=False, help_text=_('Наложить маску на изображение'))  # blank=True
    order = models.PositiveIntegerField(_('сортировка'), blank=True, default=0, help_text=_('Укажите в каком порядке сортируется слайд.'))
    link = models.CharField(_('URL кнопки'), max_length=200, blank=True, help_text=_('Если не указано, кнопка не отображается. Укажите URL адрес для кнопки. Пример: "/about/clients/"'))

    class Meta:
        db_table = 'pages_carousel'
        verbose_name = _('слайд')
        verbose_name_plural = _('карусель')
        ordering = ('order',)

    def __str__(self):
        return '%s' % self.title


@python_2_unicode_compatible
class Chank(models.Model):
    """Create chank model"""
    title = models.CharField(max_length=50, verbose_name=_('название:'), blank=False, help_text=_('Не обязательное поле!'))
    label = models.CharField(max_length=50, verbose_name=_('идентификатор:'), blank=False, help_text=_('Метка чанка!'))
    code = models.TextField(_('код:'), max_length=2000, blank=False, help_text=_('Код чанка'))
    show = models.BooleanField(_('активировать'), default=False, help_text=_('Если отмечено, чанк начнет работать'))

    class Meta:
        db_table = 'pages_chank'
        verbose_name = _('чанк')
        verbose_name_plural = _('чанк')
        ordering = ('title',)

    def __str__(self):
        return '%s' % self.title


class CustomFlatPage(FlatPage):
    class Meta:
        proxy = True

    def save(self):
        super(CustomFlatPage, self).save()
        self.sites = [Site.objects.get(pk=settings.SITE_ID)]


@python_2_unicode_compatible
class Page(CustomFlatPage):
    """Inheritance and overrides the standard flatpages model: 'sites', 'registration_required',"""
    description = models.CharField(_('описание'), max_length=200, blank=False, help_text=_('SEO поле предназначено для мета-тега description'))
    block = models.TextField(verbose_name=_('дополнительное поле'), blank=True, help_text=_('Если указано, появится  выделенный блок текста'))
    tag = models.ManyToManyField(Tag, related_name='tags', related_query_name='tag', verbose_name=_('метки'), help_text=_('SEO поле предназначено для мета-тегов keywords'))
    publishied = models.BooleanField(_('публикация'), default=False, help_text=_('Если не указано, страница не будет доступна для просмотра'))
    show = models.BooleanField(_('отображать'), default=False, help_text=_('Если отмечено, страница будет показана в главном меню'))
    order = models.PositiveIntegerField(_('сортировка'), default=0, help_text=_('Укажите в каком порядке сортируется меню. Значение меньше - выше/левее, больше - ниже/правее'))
    parent = models.CharField(_('URL родителя'), max_length=20, blank=True, help_text=_('Пример: /about/clients/. Здесь родителем является /about/. Убедитесь, что есть начальные и конечные слэши.'))

    class Meta:
        db_table = 'pages_page'
        verbose_name = _('страницу')
        verbose_name_plural = _('страница')
        ordering = ('order',)

    def __str__(self):
        return "%s -- %s" % (self.url, self.parent)
