from django import forms
from revuo.models import NewsItem, BlogItem, VideoItem, Author, Publication


class FormNewsItem(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = ('title', 'description', 'text')


class FormVideoItem(forms.ModelForm):
    class Meta:
        model = VideoItem
        fields = ('title', 'video', 'text')


class FormBlogItem(forms.ModelForm):
    class Meta:
        model = BlogItem
        fields = ('title', 'description', 'text')


class FormPublication(forms.Form):
   title = forms.CharField(max_length=140)
   description = forms.CharField(max_length=280, widget=forms.Textarea)
   attachment = forms.FileField()


class FormEditProfile(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('about',)
