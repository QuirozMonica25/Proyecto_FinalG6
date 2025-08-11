
from django.urls import path
from . import views

app_name = 'gaming'
urlpatterns = [    
    path('', views.Listar_Notigaming, name = 'listar'),

    path('Detalle/<int:pk>', views.Detalle_Notigaming, name = 'detalle'),

    path('Comentario/', views.Comentar_Notigaming, name = 'comentar'),
    
]