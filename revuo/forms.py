from django import forms
from django_summernote.widgets import SummernoteWidget
from revuo.models import NewsItem, BlogItem, Author


class FormNewsItem(forms.ModelForm):
    class Meta(object):
        model = NewsItem
        fields = ('title', 'description', 'text')
        widgets = {'text': SummernoteWidget()}


class FormBlogItem(forms.ModelForm):
    class Meta(object):
        model = BlogItem
        fields = ('title', 'description', 'text')
        widgets = {'text': SummernoteWidget()}


class FormPublication(forms.Form):
    title = forms.CharField(max_length=140)
    description = forms.CharField(max_length=280, widget=forms.Textarea)
    attachment = forms.FileField()


class FormEditProfile(forms.ModelForm):
    class Meta(object):
        model = Author
        fields = ('about',)
