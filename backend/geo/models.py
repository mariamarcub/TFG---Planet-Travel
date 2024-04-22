from django.db import models
from main.models import Client, Card

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
