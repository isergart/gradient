# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from pages.widgets import Editor
from .models import *


# Create ImageAdmin
class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    verbose_name = 'файл'
    verbose_name_plural = 'фотогалерея'
    fields = ('image', 'title', 'watermark',)


# Create NewsAdmin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'description', 'content', 'tag', 'publishied', ],
          'classes': ['extrapretty']}),
        ('Дополнительные настройки', {
            'fields': ['teaser', 'slug', 'user', 'date_created', 'social_button', ],
         'classes': ['collapse'],
         }),
         ]
    formfield_overrides = {models.TextField: {'widget': Editor}, }
    inlines = [ImageInline, ]
    filter_gorisontal = ('draft',)
    list_filter = ('publishied', 'user',)
    list_display = ('title', 'user', 'publishied',)
    list_per_page = 15
    ordering = ('-date_created',)
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ('date_created', 'social_button',)
    search_fields = ('title',)
    raw_id_fields = ['tag']


# Create ProjectsAdmin
@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    pass
