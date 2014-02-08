from django import forms

class ClientRegisteration(forms.Form):
    username = forms.CharField(max_length=100)