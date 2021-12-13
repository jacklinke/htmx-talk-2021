from django import forms

from users.models import User

class FormOne(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

class FormTwo(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

class FormThree(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

class FormFour(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

class FormFive(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
