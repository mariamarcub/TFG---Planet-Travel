from django.contrib import admin
from .models import Client
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    search_fields = ['client']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['user']