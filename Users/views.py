from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import HttpResponseForbidden

def cadastro(request):
    if request.method == "GET":
        return render(request, 'Users/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')

        if User.objects.filter(username=username).exists():
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha)

        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if not created:
            user_profile.cargo = cargo
            user_profile.save()

        return HttpResponse('Usuário cadastrado com sucesso')
    
def login(request):
    if request.method == "GET":
        return render(request, 'Users/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            remember_me = request.POST.get('remember_me', False)

            if not remember_me:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(1209600)

            try:
                user_profile = user.userprofile
                if user_profile.cargo == 'admin':
                    return redirect('admin_home')
                elif user_profile.cargo == 'tecnico':
                    return redirect('tecnico_home')
                else:
                    return HttpResponse('Cargo não definido corretamente.')
            except UserProfile.DoesNotExist:
                return HttpResponse('Perfil do usuário não encontrado.')
            
        else:
            return HttpResponse('Usuário ou senha inválidos')

@login_required(login_url="/auth/login/")#mesmo com o usuário estando logado em uma conta com cargo tecnico ao por a url de admin_home consegue acesso (erro a ser corrigido)
def admin_home(request):
    return render(request, 'Users/admin_home.html')

@login_required(login_url="/auth/login/")
def tec_home(request):
    return render(request, 'Users/tecnico_home.html')

@login_required(login_url="/auth/login/")
def admin_user_list(request):
    if not request.user.is_superuser:  # Verifica se o usuário é administrador
        return HttpResponseForbidden()
    users = User.objects.all()
    return render(request, 'Users/User_list.html', {'users': users})

@login_required(login_url="/auth/login/")
def gerenciar_acc(request):
    return render(request, 'Users/gen_acc.html',)