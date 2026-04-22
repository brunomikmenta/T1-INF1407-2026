from django import forms
from .models import User, Song

class CustomUserCreationForm(forms.ModelForm):
    nova_senha = forms.CharField(
        label='Nova senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    confirmar_senha = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:

        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nova_senha = cleaned_data.get('nova_senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if nova_senha and confirmar_senha and nova_senha != confirmar_senha:
            raise forms.ValidationError('As senhas nao conferem.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.senha = self.cleaned_data['nova_senha']

        if commit:
            user.save()

        return user


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
        exclude = ['senha']


class CreateSongList(forms.Form):
    # Song 1 fields
    song1_name = forms.CharField(label='Nome da Primeira Música', max_length=50, required=False)
    song1_artist = forms.CharField(label='Artista 1', max_length=30, required=False)
    song1_gender = forms.CharField(label='Gênero 1', max_length=30, required=False)
    
    # Song 2 fields
    song2_name = forms.CharField(label='Nome da Segunda Música', max_length=50, required=False)
    song2_artist = forms.CharField(label='Artista', max_length=30, required=False)
    song2_gender = forms.CharField(label='Gênero', max_length=30, required=False)
    
    # Song 3 fields
    song3_name = forms.CharField(label='Nome da Terceira Música', max_length=50, required=False)
    song3_artist = forms.CharField(label='Artista', max_length=30, required=False)
    song3_gender = forms.CharField(label='Gênero', max_length=30, required=False)
    
    # Song 4 fields
    song4_name = forms.CharField(label='Nome da Quarta Música', max_length=50, required=False)
    song4_artist = forms.CharField(label='Artista', max_length=30, required=False)
    song4_gender = forms.CharField(label='Gênero', max_length=30, required=False)
    
    # Song 5 fields
    song5_name = forms.CharField(label='Nome da Quinta Música', max_length=50, required=False)
    song5_artist = forms.CharField(label='Artista', max_length=30, required=False)
    song5_gender = forms.CharField(label='Gênero', max_length=30, required=False)

    def clean(self):
        cleaned_data = super().clean()
        
        # Validate that if any field of a song is filled, all fields for that song should be filled
        for i in range(1, 6):
            name = cleaned_data.get(f'song{i}_name')
            artist = cleaned_data.get(f'song{i}_artist')
            gender = cleaned_data.get(f'song{i}_gender')
            
            # If any field is filled, all should be filled
            filled_fields = [name, artist, gender]
            filled_count = sum(1 for field in filled_fields if field)
            
            if filled_count > 0 and filled_count < 3:
                raise forms.ValidationError(f'Para a Música {i}, preencha todos os campos (nome, artista e gênero) ou deixe todos vazios.')
        
        return cleaned_data


class EditSong(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'artist', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
        }