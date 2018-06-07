# -*- coding: utf-8 -*-
from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('project/tpl_project.html')
def project():
    projects = Project.objects.all()
    return {'projects': projects }
