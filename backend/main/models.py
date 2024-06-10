from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings


#MODELO CLIENTE
class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   # photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name_plural = "Clients"


#VALIDADOR DEL CVV
def validate_card(value):
    if not str(value).isdigit() or len(str(value)) != 3:
        raise ValidationError('El CVV tiene que ser de tres dígitos.')


#MODELO TARJETA
class Card(models.Model):
    client = models.ForeignKey(Client, models.PROTECT)
    owner = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    expiration = models.DateField()
    cvv = models.IntegerField(validators=[validate_card])

    def __str__(self):
        return f'{self.owner} - {self.type} - {self.expiration}'  # Son las que me interesa sacar y así no sale la misma información repetida

    class Meta:
        unique_together = ['type', 'owner']
        verbose_name_plural = "Cards"  # Para que reconozca la clase en plural también


