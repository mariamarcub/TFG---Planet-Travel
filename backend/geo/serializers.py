# serializers.py

from rest_framework import serializers
from .models import Country, Continent, Voyage, Voyager


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


class VoyagerSerializer(serializers.ModelSerializer):
    departure_city = serializers.CharField()  # Asegúrate de aceptar nombres de ciudades como CharField

    class Meta:
        model = Voyager
        fields = [
            'name', 'last_name', 'second_surname', 'email',
            'birth_date', 'telephone', 'dni', 'passport', 'departure_city'
        ]
        extra_kwargs = {
            'second_surname': {'required': False},
            # Hacer que second_surname sea opcional
            'dni': {'required': False, 'allow_null': True},
            'passport': {'required': False, 'allow_null': True}
        }

    def validate(self, data):
        dni = data.get('dni')
        passport = data.get('passport')

        if not dni and not passport:
            raise serializers.ValidationError(
                "Debe proporcionar al menos un DNI o un pasaporte.")

            # Validaciones adicionales para campos requeridos
            required_fields = ['name', 'last_name', 'email', 'birth_date',
                               'telephone', 'departure_city']
            for field in required_fields:
                if not data.get(field):
                    raise serializers.ValidationError(
                        {field: "Este campo es obligatorio."})

        return data
