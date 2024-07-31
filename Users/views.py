from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def cadastro(request):
    if request.method == "GET":
        return render(request, 'Users/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('ja existe um usuário com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        user_profile = UserProfile(user=user, cargo=cargo)
        user_profile.save()

        return HttpResponse('Usuário cadastrado com sucesso')
    

def login(request):
    if request.method == "GET":
        return render (request, 'Users/login.html')
    

    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)


        if user:
            login_django(request, user)

            remember_me = request.POST.get('remember_me',False)

            if not remember_me:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(1209600)

            return HttpResponse('autenticado')
        else:
            return HttpResponse('email ou senha inválidos')
        
@login_required(login_url="/auth/login/")
def plataforma(request):
    return HttpResponse('plataforma')