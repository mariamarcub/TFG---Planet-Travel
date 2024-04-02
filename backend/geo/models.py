from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Continents"


class Country(models.Model):
    code_iso2 = models.CharField(max_length=2, unique=True)
    code_iso3 = models.CharField(primary_key=True, max_length=3, unique=True)
    name = models.CharField(max_length=200)
    num_code = models.IntegerField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.name} - {self.num_code} - {self.continent.name}"

    class Meta:
        verbose_name_plural = "Countries"


class City(models.Model):
    code_iso2 = models.CharField(primary_key=True, max_length=2, unique=True)
    name = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.name} - {self.code_iso2} - {self.country.name}"

    class Meta:
        verbose_name_plural = "Cities"

