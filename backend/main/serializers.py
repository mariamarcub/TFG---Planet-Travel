from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

from main.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=False)

    class Meta:
        model = Client
        fields = ('username', 'first_name', 'last_name',
                  'password', 'password2', 'email')

    @staticmethod
    def validate_email(value):
        if value and User.objects.filter(email=value).exists():
            raise ValidationError("Ya existe un usuario con este correo electrónico.")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError(
                {"password": "Las contraseñas no coinciden."})
        return data

    def create(self, validated_data):
        password = validated_data['password']
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(password)
        user.save()
        client = Client.objects.create(user=user)
        return client


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return user
        raise ValidationError("Credenciales incorrectas")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'