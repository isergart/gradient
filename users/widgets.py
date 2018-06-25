# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.conf import settings
from PIL import Image
import os


class AdminImage(AdminFileWidget):
    """
    A FileField Widget that displays an image instead of a file path if the current file is an image
    """
    def thumbnail(image_path):
        """
        Missing docstring
        """
        absolute_url = os.path.join(settings.MEDIA_ROOT, image_path)
        return u'<img src="%s" alt="%s" />' % (absolute_url, image_path)

    def render(self, name, value, attrs=None):
        output = []
        file_name = str(value)
        if file_name:
            file_path = '%s%s' % (settings.MEDIA_URL, file_name)
            try:            # is image
                Image.open(os.path.join(settings.MEDIA_ROOT, file_name))
                output.append('<a target="_blank" href="%s">%s</a><br />%s <a target="_blank" href="%s">%s</a><br />%s ' %
                              (file_path, thumbnail(file_name), ('Currently:'), file_path, file_name, ('Change:')))
            except IOError:  # not image
                output.append('%s <a target="_blank" href="%s">%s</a> <br />%s ' %
                              (('Currently:'), file_path, file_name, ('Change:')))

        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
