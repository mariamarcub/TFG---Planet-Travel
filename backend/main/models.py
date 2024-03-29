from django.conf import settings
from django.db import models

class Cliente (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Pasará una cadena como modelo de clave externa.
    # Sirve para enlazar el usuario de django con la de BD

    def __str__(self):
        return f'{self.user.username}'  # username viene de una importación --> django.contribu.auth, el cual tiene el modelo USER

    class Meta:
        verbose_name_plural = "Clientes"


