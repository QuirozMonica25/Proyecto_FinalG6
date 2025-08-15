from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.db import transaction


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido', 'email', 'fecha_nacimiento', 'imagen']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = False
        if commit:
            user.save()
        return user