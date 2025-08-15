from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField()
    fecha_nacimiento = models.DateField('fecha_nacimiento', default=date(2000,1,1))
    es_colaborador = models.BooleanField(default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios', default='img/usuario_default.png')

    class Meta:
        ordering = ('-nombre',)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.username})"
    
    def get_absolute_url(self):
         return reverse('apps.usuarios:actualizar_usuario', args=[self.pk])
        