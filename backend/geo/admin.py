from django.contrib import admin

from geo.models import City


class CityAdmin(admin.ModelAdmin):
    city_columns = ['code_iso2', 'name']
    search_fields = city_columns
    list_filter = city_columns
    list_display = city_columns


admin.site.register(City, CityAdmin)