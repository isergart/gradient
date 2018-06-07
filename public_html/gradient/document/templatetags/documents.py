# -*- coding: utf-8 -*-
from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('document/tpl_partner.html')
def partners():
    tag = Partner.objects.all().filter(show=True)
    return {'tag': tag }
