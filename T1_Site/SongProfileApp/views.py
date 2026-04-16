from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'SongProfileApp/index.html')

def cadastroUsuario(request):

    if request.method == 'POST':

        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect('homepage')
    
    else:

        formulario = UserCreationForm()
    
    contexto = {'form' : formulario,}
    return render(request, 'SongProfileApp/cadastroUsuario.html', contexto)

def login(request):
    return render(request, 'SongProfileApp/login.html')

def loginComSucesso(request):

    if request.method == 'POST':
        user_input = request.POST.get('username')
        pass_input = request.POST.get('password')

        # Utiliza a função authenticate para verificar as credenciais na tabela correta do Django
        user = authenticate(request, username=user_input, password=pass_input)

        if user is not None:
            auth_login(request, user) # Inicia a sessão do usuário no navegador
            return render(request, 'SongProfileApp/loginSucesso.html')
        else:
            return render(request, 'SongProfileApp/index.html', {'error': 'Credenciais inválidas'})

    # Se for um acesso direto (GET), volta para a página de login
    return redirect('homepage')

def logout(request):

    logout(request) # Encerra a sessão do usuário
    return redirect('homepage')