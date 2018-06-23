from django import forms


# CKEditor widget
# Original flatpages {'widget': forms.Textarea(attrs={'rows': '10', 'cols': '40'})},
class Editor(forms.Textarea):
    class Media:
        css = {'all': ('pages/ckeditor/django/styles.css',)}
        js = ('admin/js/vendor/jquery/jquery.min.js', 'pages/ckeditor/ckeditor.js', 'pages/ckeditor/adapters/jquery.js', 'pages/ckeditor/django/init.js',)
