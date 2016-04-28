from django import forms
from django.contrib.auth.models import User

class FormUserLogin(forms.ModelForm):
    class Meta:
        model = User
