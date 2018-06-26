# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from users.models import User
from pages.models import Tag
from datetime import datetime
import random
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Project(models.Model):
    """
    Create Project model
    """
    CATEGORY_CHOICES = (
        ('a', _('Промышленное холодоснабжение')),
        ('b', _('Внутренние инженерные системы')),
        )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, verbose_name=_('тип обьекта'), default='a')
    pass

    class Meta:
        db_table = 'feeds_project'
        verbose_name = _('объект')
        verbose_name_plural = _('обьект')

    def __str__(self):
        return self.category


@python_2_unicode_compatible
class Post(models.Model):
    """
    Create News model
    """
    title = models.CharField(max_length=100, verbose_name=_('заголовок:'), help_text=_('Не более 100 символов (включая пробелы)'))
    description = models.CharField(_('описание:'), max_length=200, blank=False, help_text=_('SEO поле предназначено для мета-тега description'))
    teaser = models.CharField(max_length=200, verbose_name=_('аннотация:'), blank=True, help_text=_('Не обязательное поле! Заполните краткое описание поста. Не более 200 символов (включая пробелы).<br> Если оставить пустым, то возьмутся первые 200 символов из содержания статьи'))
    content = models.TextField(verbose_name=_('содержание:'), blank=True, help_text=_('Наполнение статьи.'))
    slug = models.SlugField(_('URL:'), help_text=_('человекоподобный URL поста, латинскими буквами'))
    publishied = models.BooleanField(_('публикация'), default=False, help_text=_('Если не указано, страница не будет доступна для просмотра'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('дата создания'), help_text=_('Время и дата не будет отображаться на сайте!'))
    date_publishied = models.DateTimeField(default=datetime.now, verbose_name=_('дата публикации'), help_text=_('Время публикации поста. Отображается на сайте'))
    tag = models.ManyToManyField(Tag, related_name='news_tags', related_query_name='news_tag', verbose_name=_('метки'), help_text=_('SEO поле предназначено для мета-тегов keywords'))
    social_button = models.BooleanField(default=True, verbose_name=_('разрешить перепост'), help_text=_('Добавить кнопку: "Поделиться" в Facebok, Twitter, Вконтакт, Одноклассники, Мой мир.<br> Для перепоста на свою страницу'))  # editable=False, default=False
    user = models.ForeignKey(User, verbose_name=_('автор поста'), on_delete=models.CASCADE,)
    image = models.ForeignKey('Image', related_name='news_images', blank=True, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'feeds_post'
        verbose_name = _('новость')
        verbose_name_plural = _('новость')
        ordering = ['-date_created']

    def __str__(self):
        return '%s' % self.title

    # def save(self, **kwargs):
    #     if not self.image:
    #         self.image = Image.objects.get(id=1)
    #     else:
    #         number = random.randint(1, 6)
    #         self.image = 'news/random/pic' + str(number) + '.jpg'
    #     super(Post, self).save()


@python_2_unicode_compatible
class Image(models.Model):
    """
    Create Image for Feeds
    """
    title = models.CharField(_('заголовок:'), max_length=50, blank=True, help_text=_('Не обязательное поле!'))
    image = models.ImageField(_('изображение'), upload_to='uploads/%Y/%m/%d/', blank=True, help_text=_('Размер изображения не более 1Mб. Горизонтального вида'))
    watermark = models.BooleanField(_('защита'), default=0, help_text=_('Добавляется водяной знак на фотографию'))
    # project = models.ForeignKey(Project, related_name='feed_image', verbose_name='галерея', on_delete=models.CASCADE, unique=False)
    news = models.ForeignKey(Post, related_name='post_image', verbose_name=_('галерея'), on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = 'feeds_image'
        verbose_name = _('изображение')
        verbose_name_plural = _('изображения')
        ordering = ['id']

    def __str__(self):
        return '%s' % self.title
