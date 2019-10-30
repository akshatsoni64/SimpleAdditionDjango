from django import forms


class LoginForm(forms.Form):
    a = forms.CharField(max_length=10)
    b = forms.CharField(max_length=10)