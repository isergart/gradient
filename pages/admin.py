# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .widgets import *
from .models import *


# Create new TagAdmin
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'cloud',)
    ordering = ('-name',)
    prepopulated_fields = {'slug': ['name']}
    search_fields = ('name',)


# Create new CarouselAdmin
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    pass


# Create new CarouselAdmin
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass


# Use CKEditor if available
try:
    from ckeditor_uploader.widgets import CKEditorUploadingWidget as content_widget
except ImportError:
    content_widget = models.TextField


# Define a new FlatPageAdmin
@admin.register(Page)
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'description', 'content', 'tag', 'publishied',)}),
        ('Дополнительные настройки', {
            'classes': ('collapse',),
            'fields': ('block', 'show', 'url', 'parent', 'order','sites', 'registration_required', 'template_name',),
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': content_widget }
    }
    list_display = ('title', 'show', 'url','parent',)
    list_filter = ('sites', )
    search_fields = ('url', 'title')
    ordering = ('order', 'title',)
    list_per_page = 15
    raw_id_fields = ['tag']


admin.site.unregister(FlatPage)
admin.site.site_header = 'Компания Градиент'
admin.site.index_title = 'Управление сайтом'
