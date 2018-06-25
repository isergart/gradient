# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from pages.widgets import Editor
from django import forms
# from django.forms import *
from .models import *


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': Editor}, }
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    # class Meta:
        # widgets = {
        #     'teaser': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
    formfield_overrides = {
            models.TextField: {'widget': Editor},
    }
    pass
