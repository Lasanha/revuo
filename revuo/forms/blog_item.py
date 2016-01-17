from django import forms
from django_summernote.widgets import SummernoteWidget
from revuo.models import BlogItem


class FormBlogItem(forms.ModelForm):
    class Meta(object):
        model = BlogItem
        fields = ('title', 'description', 'text')
        widgets = {'text': SummernoteWidget()}
