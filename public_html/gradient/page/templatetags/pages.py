# -*- coding: utf-8 -*-
from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('page/tpl_tag.html')
def tag():
    tag = Tag.objects.all().filter(cloud=True)
    return {'tag': tag }

@register.inclusion_tag('page/tpl_carousel.html')
def carousel():
    carousel = Tag.objects.all().filter(cloud=True)
    return {'carousel': carousel }

@register.inclusion_tag('page/tpl_snippet.html')
def snippet():
    code = Snippet.objects.all().filter(show=True)
    return {'code': code }
