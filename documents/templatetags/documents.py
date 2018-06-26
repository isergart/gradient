# -*- coding: utf-8 -*-
from django import template
from ..models import *

register = template.Library()


@register.inclusion_tag('documents/tpl_partner.html')
def partners():
    """Make partners template"""
    tag = Partner.objects.all().filter(show=True)
    return {'tag': tag}
