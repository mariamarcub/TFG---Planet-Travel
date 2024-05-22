from django.db import models
from main.models import Client, Card

# MODELO CONTINENTE
class Continent(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


#MODELO CIUDAD
class City(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.name} - {self.country.name}"

    class Meta:
        verbose_name_plural = "Cities"


#MODELO VIAJE
class Voyage(models.Model):
    #user = models.ForeignKey(Client, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField(default="Resumen")
    itinerary = models.TextField(default='Itinerario predeterminado.')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    maximum_travelers = models.IntegerField()

    def __str__(self):
        return f"{self.city.name} - {self.date_start} - {self.date_end}"

    class Meta:
        verbose_name_plural = "Voyages"


#MODELO COMPRA
class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, default=None, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=5, null=True)


    def __str__(self):
        return f"{self.client.user.username} - {self.amount} - {self.date}"

    class Meta:
        verbose_name_plural = "Purchases"


#MODELO DE VIAJEROS
class Voyager(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    second_surname = models.CharField(max_length=32)
    email = models.CharField()
    birth_date = models.DateField()
    telephone = models.CharField(max_length=16)
    dni = models.CharField(max_length=16, null=True)
    passport = models.CharField(max_length=16, null=True)
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
