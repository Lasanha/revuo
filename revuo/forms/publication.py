from django import forms


class FormPublication(forms.Form):
    title = forms.CharField(max_length=140)
    description = forms.CharField(max_length=280, widget=forms.Textarea)
    attachment = forms.FileField()
