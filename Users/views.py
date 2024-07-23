from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse_lazy

def cadastro(request):
    if request.method == "GET":
        return render(request,'Users/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse('já existe um usuario utilizando este email')
        
        user = User.objects.create(username=username, email=email)
        user.set_password(senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')

def login(request):
    if request.method == "GET":
        return render(request, 'Users/login.html')
    else :
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()

        if user:
            username = user.username
            user = authenticate(username=username, password=senha)
            
            if user:
                auth_login(request, user)  # Autentica o usuário no sistema
                return HttpResponse('Válido')
            else:
                return HttpResponse('Email ou senha inválidos')
        else:
            return HttpResponse('Email ou senha inválidos')