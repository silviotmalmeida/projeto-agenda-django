from django.shortcuts import render, get_object_or_404
# importando a biblioteca de query complexa
from django.db.models import Q, Value
# importando a biblioteca de concatenação de atributos
from django.db.models.functions import Concat
# importando a biblioteca de paginação
from django.core.paginator import Paginator
from .models import Contato  # importando a model Contato para exibição nas views
from django.contrib import messages  # importando bilbioteca de mensagens


# definindo a view index
def index(request):
    # obtendo o valor do atributo de busca s da requisição
    search_value = request.GET.get('s')

    # caso seja None, atribui ''
    if search_value == None:
        search_value = ''

    # caso o tamanho do atributo de busca s seja inferior a 3 e não esteja vazio
    if not len(search_value) > 2 and search_value != '':

        # envia uma mensagem de erro
        messages.add_message(request, messages.ERROR,
                             'Digite pelo menos 3 caracteres no campo de busca')

        # nulifica o atributo de busca
        search_value = ''

    # criando um atributo composto por nome e sobrenome para possibilitar a busca
    concat_fields = Concat('nome', Value(' '), 'sobrenome')

    # retornando os registros do banco de dados, ordenados alfabeticamente por nome
    # e filtrados pelo atributo composto nome_sobrenome ou telefone contendo o valor
    # da busca e ativo=True
    contatos = Contato.objects.annotate(

        # aplicando o atributo composto criado anteriormente
        nome_sobrenome=concat_fields

    ).filter(

        # aplicando o filtro de busca s
        Q(nome_sobrenome__icontains=search_value) | Q(
            telefone__icontains=search_value),
        ativo=True

    ).order_by('nome')

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
