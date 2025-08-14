
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notigaming, Categoria, Comentario
from django.urls import reverse_lazy


def Listar_Notigaming(request):
    contexto = {}

    id_categoria = request.GET.get('id', None)

    if id_categoria:
        n = Notigaming.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Notigaming.objects.all().order_by('-fecha')

    contexto['notigaming'] = n

    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat
    
    return render(request, 'gaming/listar.html', contexto)

    
def Detalle_Notigaming(request,pk):
    contexto = {}
    n = Notigaming.objects.get(pk = pk) #RETORNA SOLO UN OBJETO
    contexto['noticia'] = n

    c = Comentario.objects.filter(noticia= n).select_related('usuario')

    contexto['comentarios'] = c
    

    return render(request, "gaming/detalle.html", contexto)

@login_required
def Comentar_Notigaming(request):
    com = request.POST.get('comentario', None)
    usu = request.user
    game = request.POST.get('id_noticia', None)#obtengo la pk
    noticia = Notigaming.objects.get(pk=game)#busco la noticia con esa pk
    coment = Comentario.objects.create(usuario=usu, noticia= noticia, texto=com)

    return redirect('notigaming:detalle', pk=game)
    # return redirect(reverse_lazy('gaming:detalle', kwargs={'pk':game}))


