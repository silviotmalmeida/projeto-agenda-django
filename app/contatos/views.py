from django.shortcuts import render


# definindo a view index
def index(request):
    # o html deve estar na pasta templates/contatos/
    return render(request, 'contatos/index.html')
