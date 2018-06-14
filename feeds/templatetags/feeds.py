# -*- coding: utf-8 -*-
from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('feeds/tpl_news.html')
def news():
    news = Post.objects.all()
    return {'news': news }

@register.inclusion_tag('feeds/tpl_project.html')
def project():
    projects = Project.objects.all()
    return {'projects': projects }