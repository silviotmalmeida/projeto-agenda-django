# importando as dependências padrão
from django.urls import path
from . import views


urlpatterns = [
    # definindo a url da página index_login, para o path vazio
    path('', views.login, name='index_login'),
    # definindo a url da página login
    path('login/', views.login, name='login'),
    # definindo a url da página logout
    path('logout/', views.logout, name='logout'),
    # definindo a url da página cadastro
    path('cadastro/', views.cadastro, name='cadastro'),
    # definindo a url da página dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]
