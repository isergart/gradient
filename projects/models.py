# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create Project model
CATEGORY_CHOICES = (
    ('a', 'Промышленное холодоснабжение'),
    ('b', 'Внутренние инженерные системы'),
)

@python_2_unicode_compatible
class Project(models.Model):
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, verbose_name='тип обьекта', default='a')
    pass

    class Meta:
        db_table = 'projects_project'
        verbose_name = 'объект'
        verbose_name_plural = 'обьект'

    def __str__(self):
        return self.id



# Create Image for News model
@python_2_unicode_compatible
class Image(models.Model):
    title = models.CharField('заголовок:', max_length=50, blank=True, help_text='Не обязательное поле!')
    image = models.ImageField('изображение', upload_to='uploads/%Y/%m/%d/', blank=True, help_text='Размер изображения не более 1Mб. Горизонтального вида')
    watermark = models.BooleanField('защита', default=0, help_text='Добавляется водяной знак на фотографию')
    project = models.ForeignKey(Project, related_name='project_image', verbose_name='галерея', on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = 'projects_image'
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
        ordering = ['id']

    def __str__(self):
        return '%s' % self.title
