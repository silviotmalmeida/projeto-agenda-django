from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator # importando a biblioteca de paginação 
from .models import Contato  # importando a model Contato para exibição nas views


# definindo a view index
def index(request):

    # retornando os registros do banco de dados
    contatos = Contato.objects.all()

    # repassando os contatos para o paginador, definindo o limite por página
    paginator = Paginator(contatos, 1)

    # obtendo o número da página a partir da URL
    page = request.GET.get('p')

    # obtendo os contatos da página informada
    contatos = paginator.get_page(page)

    # o html deve estar na pasta templates/contatos/
    return render(request, 'contatos/index.html', {
        'contatos': contatos,
    })


# definindo a view detalhe
def detalhe(request, contato_id):

    # retornando o registro do banco de dados
    # os filtros são o id e o status ativo
    # se não encontrar, levanta um erro 404
    contato = get_object_or_404(Contato, id=contato_id, ativo=True)

    # o html deve estar na pasta templates/contatos/
    return render(request, 'contatos/detalhe.html', {
        'contato': contato,
    })
