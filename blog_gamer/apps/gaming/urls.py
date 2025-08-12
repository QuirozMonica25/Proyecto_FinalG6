
from django.urls import path, include
from . import views


app_name = 'notigaming'
urlpatterns = [    
    path('', views.Listar_Notigaming, name='listar'),

    path('detalle/<int:pk>', views.Detalle_Notigaming, name='detalle'),

    path('comentario/', views.Comentar_Notigaming, name='comentar'),

    path("usuarios/", include('apps.usuarios.urls'))
]