from __future__ import absolute_import

from django import forms
from django.template.loader import render_to_string
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt


class Editor(forms.Textarea):
    class Media:
        js = (
            'pages/ckeditor/ckeditor.js',
            'pages/ckeditor/init.js',
         )

    def __init__(self, *args, **kwargs):
        super(Editor, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, attrs, name=name)
        template_name = 'pages/tpl_editor.html'
        context = {
            'final_attrs': flatatt(final_attrs),
            'value': conditional_escape(value),
            'id': final_attrs['id'],
        }
        return mark_safe(render_to_string(template_name, context))

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs
