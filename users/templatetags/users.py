# -*- coding: utf-8 -*-
from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('users/tpl_users.html')
def users():
    user = User.objects.all().filter(show=True)
    return {'user': user }
