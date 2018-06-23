# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from pages.widgets import Editor
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
    formfield_overrides = {models.TextField: {'widget': Editor}, }
    pass
