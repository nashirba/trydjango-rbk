from django import forms


class SearchPhoto(forms.Form):
    query_set = forms.CharField(max_length=80, label='Search photo')
