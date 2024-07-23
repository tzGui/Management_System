from django.urls import path
from . import views 

urlpatterns = [
    path('cadastro/', views.cadastro, name='Cadastro'),
    path('login/', views.login, name='login')
]
