from django import forms


class SearchPhoto(forms.Form):
    query = forms.CharField(max_length=80)
