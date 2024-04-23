from django.contrib import admin
from .models import Client
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    search_fields = ['client']

class ClientAdmin(admin.ModelAdmin):
    list_display = ('get_user_username',)  # Usar el nombre del método en lugar del campo directamente

    def get_user_username(self, obj):
        return obj.user.username  # Asumiendo que 'user' es la ForeignKey y 'username' es el campo que quieres mostrar
    get_user_username.short_description = 'Username'  # Opcional: Especificar un nombre para la columna en el admin

admin.site.register(Client, ClientAdmin)