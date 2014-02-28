from django import forms
from revuo.models import NewsItem, BlogItem, VideoItem, Author, Publication


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


class FormPublication(forms.Form):
   title = forms.CharField(max_length=140)
   description = forms.CharField(max_length=280)
   attachment = forms.FileField()


class FormEditProfile(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('about',)
