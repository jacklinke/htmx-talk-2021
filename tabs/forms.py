from django import forms

from users.models import User

class FormOne(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

class FormTwo(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

class FormThree(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

class FormFour(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

class FormFive(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]
