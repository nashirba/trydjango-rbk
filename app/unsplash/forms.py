from django import forms


class SearchPhoto(forms.Form):
    Search = forms.CharField(max_length=80)
