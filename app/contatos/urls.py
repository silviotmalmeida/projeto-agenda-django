# importando as dependências padrão
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # definindo a url da página index
]
