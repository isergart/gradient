# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
from pages.widgets import Editor
from django import forms
from .models import *


class ImageInline(admin.TabularInline):
    """
    Create ImageAdmin
    """
    model = Image
    extra = 0
    verbose_name = _('файл')
    verbose_name_plural = _('фотогалерея')
    fields = ('image', 'title', 'watermark',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """
    Vacancy
    """
    formfield_overrides = {models.TextField: {'widget': Editor}, }
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """
    Partner
    """
    pass


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    """
    Block
    """
    # class Meta:
    #     widgets = {
    #         'teaser': Textarea(attrs={'cols': 80, 'rows': 20}),
    #     }
    inlines = [ImageInline, ]
    radio_fields = {'category': admin.VERTICAL}  # HORIZONTAL
    formfield_overrides = {
            models.TextField: {'widget': Editor},
        }
    pass
