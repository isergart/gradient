# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from .widgets import Editor
from .models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Create new TagAdmin"""
    model = Tag
    list_display = ('name', 'cloud',)
    ordering = ('-name',)
    prepopulated_fields = {'slug': ['name']}
    search_fields = ('name',)


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """Create CarouselAdmin"""
    pass


@admin.register(Chank)
class ChankAdmin(admin.ModelAdmin):
    """Create SnippetAdmin"""
    pass


@admin.register(Page)
class PageAdmin(FlatPageAdmin):
    """Create PageAdmin"""
    fieldsets = (
        (None, {'fields': ('title', 'description', 'content', 'tag', 'publishied',)}),
        (_('Дополнительные настройки'), {
            'classes': ('collapse',),
            'fields': ('block', 'show', 'url', 'parent', 'order', 'template_name',),
            }),
        )
    formfield_overrides = {models.TextField: {'widget': Editor}, }
    list_display = ('title', 'show', 'url', 'parent',)
    list_filter = ('sites',)
    search_fields = ('url', 'title')
    ordering = ('order', 'title',)
    list_per_page = 15
    raw_id_fields = ['tag']


admin.site.unregister(FlatPage)
admin.site.site_header = _('Компания Градиент')
admin.site.index_title = _('Управление сайтом')
