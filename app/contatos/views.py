from django.shortcuts import render

def index(request):
    return render(request, 'contatos/index.html') # definindo a view index
