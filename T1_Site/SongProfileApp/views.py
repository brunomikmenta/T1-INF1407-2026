from django.shortcuts import render, redirect
from django.core.mail import send_mail
#from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import CustomUserCreationForm, EsqueciSenhaForm, NovaSenhaForm, ConfiguracaoEdicao
from .models import User
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.decorators import user_passes_test
'''
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views import View
'''
# Create your views here.

#Provavelmente vai tirar
def home(request):
    app_user_id = request.session.get('app_user_id')
    reset = request.session.get('reset', False)
    mensagem = request.session.pop('contexto', None)
    app_user = None

    if app_user_id:
        app_user = User.objects.filter(id=app_user_id).first()

    contexto = {
        'app_user': app_user,
        'reset': reset,
        'mensagem': mensagem,
    }
    return render(request, 'SongProfileApp/index.html', contexto)

def cadastroUsuario(request):

    if request.method == 'POST':

        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():

            formulario.save()
            request.session['contexto'] = 'Cadastro realizado com sucesso. Faça login para acessar sua conta.'

            return redirect('homepage')
    
    else:

        formulario = CustomUserCreationForm()
    
    contexto = {'form' : formulario,}
    return render(request, 'SongProfileApp/cadastroUsuario.html', contexto)

def login(request):
    if request.session.get('reset') and request.session.get('reset_user_id'):
        return redirect('novasenha')

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
        request.session['contexto'] = 'Login bem-sucedido. Bem-vindo, {}!'.format(user.username)
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
    request.session['contexto'] = 'Logout realizado com sucesso.'
    return redirect('homepage')

def perfil(request):

    app_user_id = request.session.get('app_user_id')

    if not app_user_id:
        return redirect('login')
    
    app_user = User.objects.filter(id=app_user_id).first()

    return render(request, 'SongProfileApp/perfil.html', {'app_user': app_user})

def configuracao(request):

    app_user_id = request.session.get('app_user_id')

    if not app_user_id:

        return redirect('login')

    usuario = User.objects.filter(id=app_user_id).first()

    if request.method == 'POST':
        formulario = ConfiguracaoEdicao(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            request.session['contexto'] = 'Configurações atualizadas com sucesso.'
            return redirect('homepage')
    else:
        formulario = ConfiguracaoEdicao(instance=usuario)

    contexto = {'form': formulario}
    return render(request, 'SongProfileApp/configuracao.html', contexto)
    
def esqueciSenha(request):
    if request.method == 'POST':
        form = EsqueciSenhaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            
            if user:
                assunto = 'Recuperação de Senha - MySongProfileApp'
                mensagem = f'Olá {user.username},\n\nFoi solicitado a recuperação de senha para sua conta.\n\nBasta apenas apertar no botão de login novamente que você poderá definir uma nova senha.\n\nAtenciosamente,\nEquipe MySongProfileApp'
                remetente = 'pedro@bittencourt.com'
                destinatario = [email]
                
                send_mail(assunto, mensagem, remetente, destinatario)
        
                request.session['reset_user_id'] = user.id
                request.session['reset_user_email'] = user.email
                request.session['reset'] = True
                request.session['contexto'] = 'E-mail de recuperação de senha enviado. Verifique sua caixa de entrada.'

                return redirect('homepage')
            else:
                contexto = {'form': form, 'erro': 'E-mail não encontrado no sistema.'}
                
                return render(request, 'SongProfileApp/esqueceuSenha.html', contexto)
    else:
        form = EsqueciSenhaForm()
    
    return render(request, 'SongProfileApp/esqueceuSenha.html', {'form': form})

def novaSenha(request):
    reset_user_id = request.session.get('reset_user_id')

    if not reset_user_id:
        return redirect('esquecisenha')

    user = User.objects.filter(id=reset_user_id).first()
    if not user:
        request.session.pop('reset_user_id', None)
        request.session.pop('reset_user_email', None)
        request.session.pop('reset', None)
        return redirect('esquecisenha')

    if request.method == 'POST':
        form = NovaSenhaForm(request.POST)
        if form.is_valid():
            user.senha = form.cleaned_data['nova_senha']
            user.save()

            request.session.pop('reset_user_id', None)
            request.session.pop('reset_user_email', None)
            request.session.pop('reset', None)

            contexto = {'error': 'Senha alterada com sucesso. Faca login novamente.'}
            return render(request, 'SongProfileApp/login.html', contexto)
    else:
        form = NovaSenhaForm()

    contexto = {
        'form': form,
        'reset_email': request.session.get('reset_user_email'),
    }
    return render(request, 'SongProfileApp/loginNovaSenha.html', contexto)

'''
class atualizaContato(View):
    def get(self, request, pk, *args, **kwargs):
        usuario = User.objects.get(id=pk)
        formulario = CustomUserCreationForm(instance=usuario)
        contexto = {'form': formulario,}
        return render(request, 'SongProfileApp/atualizaContato.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        
        usuario = User.objects.get(id=pk)
        formulario = CustomUserCreationForm(request.POST, instance=usuario)
        if formulario.is_valid():
            usuario = formulario.save()
            return HttpResponseRedirect(reverse_lazy('homepage'))
        
        else:

            contexto = {'form': formulario,}
            return render(request, 'SongProfileApp/atualizaContato.html', contexto)
        
'''