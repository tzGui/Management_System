from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('admin_home/', views.admin_home, name='admin_home'),#usuarios com cargo de tecnico não deveriam possuir acesso
    path('tecnico_home/', views.tec_home, name='tecnico_home'),
    path('admin/users/', views.admin_user_list, name='admin_user_list'),#resolver problema de autenticação
    path('gerenciamento_de_contas/', views.gerenciar_acc, name='gerenciar_contas')
]