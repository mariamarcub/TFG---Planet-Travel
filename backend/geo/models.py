from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

#MODELO CLIENTE
class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def _str_(self):
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

    def _str_(self):
        return f'{self.owner} - {self.type} - {self.expiration}'  # Son las que me interesa sacar y así no sale la misma información repetida

    class Meta:
        unique_together = ['type', 'owner']
        verbose_name_plural = "Cards"  # Para que reconozca la clase en plural también


# MODELO CONTINENTE
class Continent(models.Model):
    name = models.CharField(max_length=200)

    def _str_(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Continents"


# MODELO PAÍS
class Country(models.Model):
    code_iso2 = models.CharField(max_length=2, unique=True)
    code_iso3 = models.CharField(primary_key=True, max_length=3, unique=True)
    name = models.CharField(max_length=200)
    num_code = models.IntegerField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


#MODELO CIUDAD
class City(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)


    def _str_(self):
        return f"{self.name} - {self.country.name}"

    class Meta:
        verbose_name_plural = "Cities"


#MODELO COMPRA
class Purchase(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def _str_(self):
        return f"{self.user.user.username} - {self.card.owner} - {self.date} - {self.price}"

    class Meta:
        verbose_name_plural = "Purchases"

#MODELO VIAJE
class Voyage(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    itinerary = models.TextField(default='Itinerario predeterminado.')

    def _str_(self):
        return f"{self.user.user.username} - {self.city.name} - {self.date}"

    class Meta:
        verbose_name_plural ="Voyages"
