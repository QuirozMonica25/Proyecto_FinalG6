"""
URL configuration for blog_gamer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from operator import index
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from .import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth


#def index(request):
   # return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.Home, name='home'),
    
    path('nosotros/', views.Nosotros, name='nosotros'),
    
   path('notigaming/', include(('apps.gaming.urls', 'notigaming'), namespace='notigaming')),

    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    path('logout/',auth.LogoutView.as_view(), name="logout"),
    
    path('usuarios/', include(('apps.usuarios.urls', 'usuarios'), namespace='usuarios')),
    
    path('contacto/', views.Contacto, name='contacto'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)