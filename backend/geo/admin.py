from django.contrib import admin
from .models import City, Voyager
from .models import Country
from .models import Continent
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


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    search_fields = ['client', 'card']

@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    search_fields = ['city__name', 'date', 'itinerary']
    list_display = ['get_city_name']
    def get_city_name(self, obj):
        return obj.city.name if obj.city else ''  # Si el país está definido, devuelve su nombre; de lo contrario, devuelve una cadena vacía

    get_city_name.short_description = 'City'  # Esto define cómo se mostrará el nombre de la columna en el admin


@admin.register(Voyager)
class VoyagerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'last_name', 'first_name']