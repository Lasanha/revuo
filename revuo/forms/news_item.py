from django import forms
from django_summernote.widgets import SummernoteWidget
from revuo.models import NewsItem


class FormNewsItem(forms.ModelForm):
    class Meta(object):
        model = NewsItem
        fields = ('title', 'description', 'text')
        widgets = {'text': SummernoteWidget()}
