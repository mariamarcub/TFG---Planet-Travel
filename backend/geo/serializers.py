# serializers.py

from rest_framework import serializers
from .models import Country, Continent


class MonthSerializer(serializers.Serializer): #Como no estamos usando un modelo, por eso usamos serializers.Serializer
    id = serializers.IntegerField()
    date = serializers.CharField()


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
