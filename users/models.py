# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):
    """
    Create abstract user model
    Expansion of django.contrib.auth.models.User fields: id, username, password, first_name, last_name, email, os_active, is_staff, is_superuser, group, user_permissions, last_login, date_joined
    """
    third_name = models.CharField('отчество:', max_length=30, blank=True)
    avatar = models.ImageField('аватар', upload_to='users/', max_length=250, blank=True, help_text='Размер не более 1Mб')
    position = models.CharField('должность:', max_length=30, blank=True)
    phone = models.CharField('телефон:', max_length=30, blank=True)
    show = models.BooleanField('отображать', default=False, help_text='Отображать профиль на сайте')

    class Meta:
        db_table = 'users_user'
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудник'
        ordering = ('username',)

    def __str__(self):
        return "%s" % self.get_full_name()

    def save(self, **kwargs):
        if not self.avatar:
            self.avatar = 'users/img/default_user.jpg'
        super(User, self).save()
