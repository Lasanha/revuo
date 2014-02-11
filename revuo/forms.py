from django import forms
from models import NewsItem, BlogItem, VideoItem


class FormNewsItem(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = ('title', 'text', 'description')


class FormVideoItem(forms.ModelForm):
    class Meta:
        model = VideoItem
        fields = ('title', 'video', 'text')


class FormBlogItem(forms.ModelForm):
    class Meta:
        model = BlogItem
        fields = ('title', 'text', 'description')