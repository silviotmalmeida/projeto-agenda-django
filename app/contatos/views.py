# rederização das views e redirecionamento entre views
from django.shortcuts import render, get_object_or_404, redirect
# importando a biblioteca de query complexa
from django.db.models import Q, Value
# importando a biblioteca de concatenação de atributos
from django.db.models.functions import Concat
# importando a biblioteca de paginação
from django.core.paginator import Paginator
from .models import Contato, Categoria  # importando as models para exibição nas views
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
    paginator = Paginator(contatos, 7)

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


# definindo a view loadtestdata
# tem a função de carregar uma massa de dados de teste
def loadtestdata(request):

    # lista das categorias a serem criadas
    categoriasTestData = [
        {'nome': 'Amigos'},
        {'nome': 'Família'},
        {'nome': 'Trabalho'},                
    ]

    # iterando sobre o array de categorias
    for categoriaTestData in categoriasTestData:

        # cadastrando a nova categoria
        categoria = Categoria.objects.create(nome=categoriaTestData['nome'])
        categoria.save()

    # lista dos contatos a serem criados
    contatosTestData = [
        {'nome': 'Vaiwu', 'sobrenome': 'Guas', 'telefone':'123456', 'email':'guas@email.com', 'descricao':'descricao Guas', 'categoria_id':1},
        {'nome': 'Koebeoza', 'sobrenome': 'Cenes', 'telefone':'123456', 'email':'cenes@email.com', 'descricao':'descricao Cenes', 'categoria_id':2},
        {'nome': 'Asnos', 'sobrenome': 'Gyeor', 'telefone':'123456', 'email':'gyeor@email.com', 'descricao':'descricao Gyeor', 'categoria_id':3},

        {'nome': 'Woiviosi', 'sobrenome': 'Ponudo', 'telefone':'123456', 'email':'ponudo@email.com', 'descricao':'descricao Ponudo', 'categoria_id':1},
        {'nome': 'Brabya', 'sobrenome': 'Boytuvor', 'telefone':'123456', 'email':'boytuvor@email.com', 'descricao':'descricao Boytuvor', 'categoria_id':2},
        {'nome': 'Sarun', 'sobrenome': 'Myohain', 'telefone':'123456', 'email':'myohain@email.com', 'descricao':'descricao Myohain', 'categoria_id':3},

        {'nome': 'Esxayse', 'sobrenome': 'Boefa', 'telefone':'123456', 'email':'boefa@email.com', 'descricao':'descricao Boefa', 'categoria_id':1},
        {'nome': 'Leges', 'sobrenome': 'Gyon', 'telefone':'123456', 'email':'gyon@email.com', 'descricao':'descricao Gyon', 'categoria_id':2},
        {'nome': 'Kakes', 'sobrenome': 'Kaumo', 'telefone':'123456', 'email':'kaumo@email.com', 'descricao':'descricao Kaumo', 'categoria_id':3},
    ]

    # iterando sobre o array de contatos
    for contatoTestData in contatosTestData:
    
        # cadastrando o novo contato
        contato = Contato.objects.create(nome=contatoTestData['nome'], sobrenome=contatoTestData['sobrenome'],
                                        telefone=contatoTestData['telefone'], email=contatoTestData['email'],
                                        descricao=contatoTestData['descricao'], categoria_id=contatoTestData['categoria_id'])
        contato.save()

    # redirecionando para a página de index
    return redirect('index')


