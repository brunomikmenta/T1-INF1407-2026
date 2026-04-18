from django import forms
from .models import User

class CustomUserCreationForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'senha']


class EsqueciSenhaForm(forms.Form):
    email = forms.EmailField(label='E-mail')


class NovaSenhaForm(forms.Form):
    nova_senha = forms.CharField(label='Nova senha', widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(label='Confirmar nova senha', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        nova_senha = cleaned_data.get('nova_senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if nova_senha and confirmar_senha and nova_senha != confirmar_senha:
            raise forms.ValidationError('As senhas nao conferem.')

        return cleaned_data
    
class ConfiguracaoEdicao(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'