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
   # first_name = serializers.CharField(required=True)
   # last_name = serializers.CharField(required=False) #No es obligatorio aportar un segundo apellido
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Client
        fields = ('username', 'password', 'password2', 'email')

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
    # Definimos campos adicionales que pertenecen al modelo User
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'email']


    # Método para actualizar tanto el modelo Client como el modelo User
    def update(self, instance, validated_data):
        # Extraemos los datos del usuario del diccionario de datos validados
        user_data = validated_data.pop('user', {})
        # Obtenemos el usuario asociado al cliente
        user = instance.user

        # Actualizamos el cliente usando el método update de la superclase
        instance = super().update(instance, validated_data)

        # Actualizamos los campos del usuario si están presentes en los datos validados
        if user_data:
            user.username = user_data.get('username', user.username)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.email = user_data.get('email', user.email)

            # Guardamos los cambios en el modelo User
            user.save()

        return instance
