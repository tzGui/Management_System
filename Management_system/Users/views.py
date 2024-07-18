from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render (request,"usuarios/login.html")
def users_list(request):
    return render (request, "usuarios/")
def cad_user(request):
    return render (request, "usuarios/cad_users.html")