# -*- coding: utf-8 -*-
from django import template
from ..models import *

register = template.Library()


@register.inclusion_tag('pages/tpl_tag.html')
def tag():
    tag = Tag.objects.all().filter(cloud=True)
    return {'tag': tag}


@register.inclusion_tag('pages/tpl_carousel.html')
def carousel():
    carousel = Tag.objects.all().filter(cloud=True)
    return {'carousel': carousel}


@register.inclusion_tag('pages/tpl_chank.html')
def chank():
    code = Chank.objects.all().filter(show=True)
    return {'code': code}
