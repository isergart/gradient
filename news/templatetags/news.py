# -*- coding: utf-8 -*-
from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('news/tpl_news.html')
def news():
    news = Post.objects.all()
    return {'news': news }
