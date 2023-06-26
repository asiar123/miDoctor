from django.urls import path
from user.views import RegistrarUsuario, ListadoUsuario, InicioUsuarios, PerfilUsuario

urlpatterns = [
    path('listado_usuarios/', ListadoUsuario.as_view(),{'parametro_extra': 'Hola!'},name='listar_usuarios'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name = 'registrar_usuario'),
    path('inicio_usuarios/', InicioUsuarios.as_view(), name='inicio_usuarios'),
    path('perfil_usuario/', PerfilUsuario.as_view(), name='inicio_usuarios'),
]