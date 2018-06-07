# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save, pre_delete
from .utils import *


# Create User model
@python_2_unicode_compatible
class User(AbstractUser):
    '''
    Expansion of django.contrib.auth.models.User fields: id, username, password, first_name, last_name, email, os_active, is_staff, is_superuser, group, user_permissions, last_login, date_joined
    '''
    third_name = models.CharField('отчество:',max_length=30, blank=True)
    avatar = models.ImageField('аватар', upload_to = 'users/', max_length=250, blank=True, help_text='Размер не более 1Mб')
    position = models.CharField('должность:',max_length=30, blank=True)
    phone = models.CharField('телефон:',max_length=30, blank=True)
    show = models.BooleanField('отображать', default=False, help_text='Отображать профиль на сайте')

    class Meta:
        db_table = 'users_user'
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудник'
        ordering = ('username',)

    def __str__(self):
        return "%s" % self.username

    def save(self, **kwargs):
        if not self.avatar:
            self.avatar = 'users/default_user.jpg'
        super(User, self).save()

        def get_thumbnail_html(self):
            html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
            return html % (self.avatar.url, get_thumbnail_url(self.avatar.url), self.position)
        get_thumbnail_html.short_description = 'thumbnail'
        get_thumbnail_html.allow_tags = True

        def post_save_handler(sender, **kwargs):
            create_thumbnail(kwargs['instance'].avatar.path)
        post_save.connect(post_save_handler, sender=User)

        def pre_delete_handler(sender, **kwargs):
            delete_thumbnail(kwargs['instance'].avatar.path)
        pre_delete.connect(pre_delete_handler, sender=User)
