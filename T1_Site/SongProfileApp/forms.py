from django import forms
from .models import User

class CustomUserCreationForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'senha']

