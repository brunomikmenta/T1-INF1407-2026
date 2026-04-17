from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import CustomUserCreationForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def home(request):
    app_user_id = request.session.get('app_user_id')
    app_user = None

    if app_user_id:
        app_user = User.objects.filter(id=app_user_id).first()

    return render(request, 'SongProfileApp/index.html', {'app_user': app_user})

def cadastroUsuario(request):

    if request.method == 'POST':

        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect('homepage')
    
    else:

        formulario = CustomUserCreationForm()
    
    contexto = {'form' : formulario,}
    return render(request, 'SongProfileApp/cadastroUsuario.html', contexto)

def login(request):
    return render(request, 'SongProfileApp/login.html')


def loginComSucesso(request):

    if request.method != 'POST':
        return redirect('login')

    user_input = request.POST.get('username', '').strip()
    pass_input = request.POST.get('password', '')

    user = User.objects.filter(username=user_input, senha=pass_input).first()

    if user is not None:
        request.session['app_user_id'] = user.id
        request.session['app_username'] = user.username
        return redirect('homepage')
    else:
        contexto = {
            'error': 'As informações estão erradas. Verifique usuário e senha.'
        }
        return render(request, 'SongProfileApp/login.html', contexto)

    
'''
def testaAcesso(user):

    if user.has_perm('auth.add_user'):
        return True

    else:

        return False
'''
        
'''
@login_required
@user_passes_test(testaAcesso)
def loginComSucesso(request):

    teste = {
        'username': request.POST.get('username'),
        'password': request.POST.get('password'),
    }

    return render(request, 'SongProfileApp/index.html', teste)
'''


def logout(request):
    request.session.flush()
    return redirect('homepage')

def perfil(request):

    app_user_id = request.session.get('app_user_id')

    if not app_user_id:
        return render(request, 'SongProfileApp/login.html')
    
    app_user = User.objects.filter(id=app_user_id).first()

    return render(request, 'SongProfileApp/perfil.html', {'app_user': app_user})