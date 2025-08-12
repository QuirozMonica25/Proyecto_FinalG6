
from django.db import models
from apps.usuarios.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length = 60)

    def __str__(self):
        return self.nombre

class Notigaming(models.Model):
    titulo = models.CharField(max_length = 150)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='Notigaming')
    categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE, )
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField(max_length=1500)
    noticia = models.ForeignKey(Notigaming, on_delete= models.CASCADE, related_name='comentarios')
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return (f"{self.noticia}-->{self.texto}")