# -*- coding: utf-8 -*-
from django import forms


class Editor(forms.Textarea):
    """CKEditor widget"""
    class Media:
        css = {'all': ('pages/ckeditor/django/styles.css',)}
        js = ('admin/js/vendor/jquery/jquery.min.js', 'pages/ckeditor/ckeditor.js', 'pages/ckeditor/adapters/jquery.js', 'pages/ckeditor/django/init.js',)
