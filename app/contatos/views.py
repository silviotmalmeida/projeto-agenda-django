from django.shortcuts import render
from .models import Contato  # importando a model Contato para exibição nas views


# definindo a view index
def index(request):

    # retornando os registros do banco de dados
    contatos = Contato.objects.all()

    # o html deve estar na pasta templates/contatos/
    return render(request, 'contatos/index.html', {
        'contatos': contatos,
    })
