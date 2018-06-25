# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .widgets import AdminImage
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    UserAdmin
    """
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'show')}),
        ('Персональная информация', {
            'fields': ('avatar', 'first_name', 'third_name', 'last_name', 'position', 'email', 'phone',)}),
        ('Права доступа', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    formfield_overrides = {models.ImageField: {'widget': AdminImage}, }
    list_display = ('username', 'avatar', 'email', 'first_name', 'last_name', 'is_staff', 'show',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
