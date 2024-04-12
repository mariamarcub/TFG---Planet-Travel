from django.contrib import admin
from .models import City
from .models import Country
from .models import Continent
from .models import Client
from .models import Card
from .models import Purchase
from .models import Voyage


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'longitude', 'latitude', 'country']
    list_filter = ['country__continent__name']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['code_iso2', 'name']
    list_display = ['name']


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    # list_filter = ['country_continent_name']
    list_display = ['name']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    search_fields = ['client']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['user']


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    search_fields = ['user', 'card']


@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    search_fields = ['user', 'city__name', 'date', 'itinerary']