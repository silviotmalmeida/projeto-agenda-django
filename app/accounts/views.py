# rederização das views e redirecionamento entre views
from django.shortcuts import render, redirect
# mensagens e autenticação
from django.contrib import messages, auth
# validador de email do django
from django.core.validators import validate_email
# importando o model de usuários da área administrativa do django
from django.contrib.auth.models import User
# decorador para verificar se o usuário está logado
from django.contrib.auth.decorators import login_required


# definindo a view login
def login(request):

    # se a requisição não for do tipo POST
    if request.method != 'POST':
        # renderiza o formulário de login
        return render(request, 'accounts/login.html')

    # se a requisição for do tipo POST, obtem-se os dados da requisição
    usuario = request.POST.get('login')
    senha = request.POST.get('password')

    # autenticando na tabela user da área administrativa do django
    user = auth.authenticate(request, username=usuario, password=senha)

    # caso a autenticação falhe
    if not user:
        # exibe mensagem de erro
        messages.error(request, 'Usuário ou senha inválidos.')
        # renderiza o formulário de login
        return render(request, 'accounts/login.html')

    # caso a autenticação seja com sucesso
    else:
        # realiza o login no sistema
        auth.login(request, user)
        # exibe mensagem de sucesso
        messages.success(request, 'Você fez login com sucesso.')
        # renderiza o dashboard
        return redirect('dashboard')


# definindo a view logout
def logout(request):
    # realiza o logout no sistema
    auth.logout(request)
    # redireciona para o login
    return redirect('login')


# definindo a view cadastro
def cadastro(request):
    # se a requisição não for do tipo POST
    if request.method != 'POST':
        # renderiza o formulário de cadastro
        return render(request, 'accounts/cadastro.html')

    # se a requisição for do tipo POST, obtem-se os dados da requisição
    nome = request.POST.get('firstname')
    sobrenome = request.POST.get('lastname')
    email = request.POST.get('email')
    usuario = request.POST.get('login')
    senha = request.POST.get('password')
    senha2 = request.POST.get('confirm_password')

    # se existir algum campo vazio
    if not nome or not sobrenome or not email or not usuario or not senha \
            or not senha2:
        # exibe mensagem de erro
        messages.error(request, 'Nenhum campo pode estar vazio.')
        # renderiza o formulário de cadastro
        return render(request, 'accounts/cadastro.html')

    # tratamento de exceções
    try:
        # validando o email
        validate_email(email)
    # em caso de erro
    except:
        # exibe mensagem de erro
        messages.error(request, 'Email inválido.')
        # renderiza o formulário de cadastro
        return render(request, 'accounts/cadastro.html')

    # se a senha tiver tamanho inferior a 6
    if len(senha) < 6:
        # exibe mensagem de erro
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        # renderiza o formulário de cadastro
        return render(request, 'accounts/cadastro.html')

    # se o usuário tiver tamanho inferior a 6
    if len(usuario) < 6:
        # exibe mensagem de erro
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        # renderiza o formulário de cadastro
        return render(request, 'accounts/cadastro.html')

    # se a confirmação da senha não estiver válida
    if senha != senha2:
        # exibe mensagem de erro
        messages.error(request, 'Senhas não conferem.')
        # renderiza o formulário de cadastro
        return render(request, 'accounts/cadastro.html')

    # verifica na tabela user da área administrativa do django
    # se já existe um usuário com mesmo username
    # se existir:
    if User.objects.filter(username=usuario).exists():
        # exibe mensagem de erro
        messages.error(request, 'Usuário já existe.')
        # renderiza o formulário de cadastro
        return render(request, 'accounts/cadastro.html')

    # verifica na tabela user da área administrativa do django
    # se já existe um usuário com mesmo email
    # se existir:
    if User.objects.filter(email=email).exists():
        # exibe mensagem de erro
        messages.error(
            request, 'E-mail já está sendo utilizado por outro usuário.')
        # renderiza o formulário de cadastro
        return render(request, 'accounts/cadastro.html')

    # cadastrando o novo usuário na tabela user da área administrativa do django
    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()

    # exibe mensagem de sucesso
    messages.success(request, 'Cadastrado com sucesso! Agora faça login.')

    # redirecionando para a página de login
    return redirect('login')

# definindo a view dashboard
# só será permitido o acesso de usuários logados
# caso não esteja logado, redireciona para a view login
@login_required(redirect_field_name='login')
def dashboard(request):
    # renderiza o formulário de dashboard
    return render(request, 'accounts/dashboard.html')
