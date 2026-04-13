from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def home(request):
    return render(request, 'SongProfileApp/index.html')

def loginComSucesso(request):

    if request.method == 'POST':
        user_input = request.POST.get('username')
        pass_input = request.POST.get('password')

        user = User.objects.filter(username=user_input, password=pass_input).first()

        if user:

            return render(request, 'SongProfileApp/loginSucesso.html')
        else:
            return render(request, 'SongProfileApp/index.html', {'error': 'Credenciais inválidas'})

    # Se for um acesso direto (GET), volta para a página de login
    return redirect('homepage')
