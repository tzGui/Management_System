from django.contrib import admin
from django.urls import path

from Users.views import users_list, login, cad_user
from router.views import home, hometec, formulario, fluxo_geral, fluxo_unico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('usuarios/', users_list),
    path('cadastro/', cad_user),
    path('', home),
    path('tec/', hometec),
    path('formulario/', formulario),
    path('gerenciar/', fluxo_geral),
    path('unico/', fluxo_unico),
]
