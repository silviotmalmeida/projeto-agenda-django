# importando as dependências padrão
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # definindo a url da página index
    path('<int:contato_id>', views.detalhe, name='detalhe'),  # definindo a url da página detalhe
    path('loadtestdata', views.loadtestdata, name='loadtestdata'),  # definindo a url para carregamento de dados de teste
]
