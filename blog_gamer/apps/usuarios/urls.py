from django.urls import path
from .views import RegistroUsuario, ActualizarUsuario, listar_usuarios
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'apps.usuarios'

urlpatterns = [
    path("registrar/", RegistroUsuario.as_view(), name='registrar'),
    path("iniciar_sesion/", LoginView.as_view(template_name ="usuarios/login.html"),name='iniciar_sesion'),
    path("cerrar_sesion/", LogoutView.as_view(), name='cerrar_sesion'),
    path("actualizar_usuario/<int:pk>", ActualizarUsuario.as_view(), name ='actualizar_usuario'),
    path("listar_usuarios/", listar_usuarios, name ='listar_usuarios')

]