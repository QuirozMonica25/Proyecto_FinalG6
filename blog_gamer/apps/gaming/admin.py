
from django.contrib import admin


# Register your models here.

from .models import Categoria, Notigaming, Comentario
admin.site.register(Categoria)
admin.site.register(Notigaming)
admin.site.register(Comentario)