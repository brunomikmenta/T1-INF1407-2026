"""
URL configuration for T1_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from SongProfileApp import views
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.urls.base import reverse_lazy

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='homepage'),
    path("login/", views.login, name='login'),
    path("loginSucesso/", views.loginComSucesso, name='loginsucesso'),
    path("cadastroUsuario/", views.cadastroUsuario, name='cadastrousuario'), 
    path("perfil/", views.perfil, name='perfil'),
    path('logout/', views.logout, name='logout'),
    path('configuracao/', views.configuracao, name='configuracao'),
    #path('esqueciSenha/', PasswordResetView.as_view(template_name='SongProfileApp/esqueceuSenha.html', success_url=reverse_lazy('login')), name='esquecisenha'),
    path('esqueciSenha/', views.esqueciSenha, name='esquecisenha'),
    path('novaSenha/', views.novaSenha, name='novasenha'),
    path('criaLista/', views.createSongListView, name='crialista'),
    path('editSong/<int:song_id>/', views.edit_song, name='editsong'),
    path('deleteSong/<int:song_id>/', views.delete_song, name='deletesong'),
    #path('configuracao/<int:id>/', views.atualizaContato.as_view(), name='atualizaContato'),
]
