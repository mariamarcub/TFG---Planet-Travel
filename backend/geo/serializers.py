# serializers.py
from datetime import timezone

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Country, Continent, Voyage, Voyager, Client, Opinion, Purchase


class MonthSerializer(serializers.Serializer): #Como no estamos usando un modelo, por eso usamos serializers.Serializer
    id = serializers.IntegerField()
    date = serializers.CharField()

class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyage
        fields = ['__all__']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'

class AgeGroupSerializer(serializers.Serializer):
    age = serializers.CharField()
    id = serializers.IntegerField()



class VoyagerSerializer(serializers.ModelSerializer):
    departure_city = serializers.CharField()  # Asegúrate de aceptar nombres de ciudades como CharField

    class Meta:
        model = Voyager
        fields = [
            'name', 'last_name', 'email',
            'birth_date', 'telephone', 'dni', 'passport', 'departure_city'
        ]

    def validate(self, data):
        dni = data.get('dni')
        passport = data.get('passport')

        if not dni and not passport:
            raise serializers.ValidationError(
                "Debe proporcionar al menos un DNI o un pasaporte."
            )
        return data


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['id', 'purchase', 'rating', 'comment', 'report_date']

