from django.contrib import admin

from .models import City, Country, Continent


class CityAdmin(admin.ModelAdmin):
    search_fields = ['code_iso2', 'name']
    # list_filter = ['country_continent_name']
    # list_display = ['country_continent_name']


class CountryAdmin(admin.ModelAdmin):
    search_fields = ['code_iso2', 'name']
    # list_filter = ['continent__name']
    # list_display = ['continent__name']


class ContinentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    # list_filter = ['name']
    # list_display = ['name']


admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Continent, ContinentAdmin)