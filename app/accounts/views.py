from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def cadastro(request):

    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    login = request.POST.get('login')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
