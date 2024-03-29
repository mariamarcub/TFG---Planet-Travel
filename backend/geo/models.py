from django.db import models


class City(models.Model):
    code_iso2 = models.CharField(primary_key=True, max_length=2, unique=True, null=True)
    name = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)

    def __str__(self):
        return f"{self.name} - {self.code_iso3}"

    class Meta:
        verbose_name_plural = "Cities"


class Country(models.Model):
    code_iso2 = models.CharField(max_length=2, unique=True, null=True)
    code_iso3 = models.CharField(primary_key=True, max_length=3, unique=True)
    name = models.CharField(max_length=200)
    num_code = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.num_code} - {self.city.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Continent(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.country}"

    class Meta:
        verbose_name_plural = "Continents"
