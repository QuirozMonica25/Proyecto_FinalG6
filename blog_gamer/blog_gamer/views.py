
from django.views.generic import TemplateView
from django.shortcuts import render





def Home(request):
	return render(request, 't_home.html')

def Nosotros(request):
    return render(request, 't_nosotros.html')

def Contacto(request):
    return render(request, 't_contacto.html')



#def index(request):
   # return render(request, 'index.html')