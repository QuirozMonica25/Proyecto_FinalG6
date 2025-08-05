
from django.views.generic import TemplateView
from django.shortcuts import render






class HomeView(TemplateView):
    template_name= 'index.html'




#def index(request):
   # return render(request, 'index.html')