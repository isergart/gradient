# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    verbose_name = 'файл'
    verbose_name_plural = 'фотогалерея'
    fields = ('image', 'title', 'watermark',)


# Use CKEditor if available
# try:
#     from ckeditor_uploader.widgets import CKEditorUploadingWidget as content_widget
# except ImportError:
#     content_widget = models.TextField


@admin.register(Post)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': [ 'title', 'description', 'content', 'tag', 'publishied',],
         'classes': ['extrapretty']}),
        ('Дополнительные настройки', {
        'fields': ['teaser', 'slug', 'user', 'date_created', 'social_button',],
         'classes': ['collapse'],
         }),
    ]
    # formfield_overrides = {
    #     models.TextField: {'widget': content_widget}
    # }
    inlines = [ImageInline,]
    filter_gorisontal = ('draft',)
    list_filter = ('publishied', 'user',)
    list_display = ('title', 'user', 'publishied',)
    list_per_page = 15
    ordering = ('-date_created',)
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ('date_created', 'social_button',)
    search_fields = ('title',)
    raw_id_fields = ['tag']
