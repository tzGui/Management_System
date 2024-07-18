from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render (request,"gerenciamento/home.html")
def hometec(request):
    return render (request, "gerenciamento/hometec.html")
def formulario(request):
    return render (request, "gerenciamento/formulario.html")
def fluxo_geral(request):
    return render (request, "gerenciamento/fluxo_geral.html")
def fluxo_unico(request):
    return render (request, "gerenciamento/fluxo_unico.html")