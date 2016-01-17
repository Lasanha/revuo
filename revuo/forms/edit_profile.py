from django import forms
from revuo.models import Staff


class FormEditProfile(forms.ModelForm):
    class Meta(object):
        model = Staff
        fields = ('about',)
