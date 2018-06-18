from __future__ import absolute_import

from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django.template.loader import render_to_string
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt


class LazyEncoder(DjangoJSONEncoder):
    pass


json_encode = LazyEncoder().encode


DEFAULT_CONFIG = {
    # 'skin': 'moono-lisa',
    'toolbar_Basic': [
        ['Source', '-', 'Bold', 'Italic']
    ],
    'toolbar_Full': [
                ['Undo', 'Redo', '-', 'Bold', 'Italic', '-', 'NumberedList', 'BulletedList', 'Format', 'RemoveFormat'],
                ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
                ['Link', 'Unlink', 'Anchor', 'Image', 'HorizontalRule'],
                ['Templates', 'Templates2', 'ShowBlocks', 'Source', '-', 'Maximize', ],
        ],
    'toolbar': 'Full',  # Basic
    # 'removePlugins': ','.join([
    #             'stylesheetparser',
    #     ]),
    #         'extraPlugins': ','.join([
    #             'uploadimage',
    #     ]),
    'allowedContent': True,
    # 'height': 200,
    # 'width': 800,
    # 'filebrowserWindowWidth': 940,
    # 'filebrowserWindowHeight': 725,
}


class CKEditor(forms.Textarea):
    class Media:
        js = ('pages/ckeditor/ckeditor_init.js', 'pages/ckeditor/ckeditor.js')

    def __init__(self, config_name='default', extra_plugins=None, external_plugin_resources=None, *args, **kwargs):
        super(CKEditor, self).__init__(*args, **kwargs)
        self.config = DEFAULT_CONFIG.copy()
        extra_plugins = extra_plugins or []

        if extra_plugins:
            self.config['extraPlugins'] = ','.join(extra_plugins)

        self.external_plugin_resources = external_plugin_resources or []

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, attrs, name=name)
        template_name = 'pages/tpl_ckeditor.html'
        external_plugin_resources = [[force_text(a), force_text(b), force_text(c)]for a, b, c in self.external_plugin_resources]
        context = {
            'final_attrs': flatatt(final_attrs),
            'value': conditional_escape(value),
            'id': final_attrs['id'],
            'config': json_encode(self.config),
            'external_plugin_resources': json_encode(external_plugin_resources)
        }
        return mark_safe(render_to_string(template_name, context))

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs
