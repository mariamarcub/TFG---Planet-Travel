from django.contrib.auth import login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Client
from main.serializers import ClientRegisterSerializer, LoginSerializer, ProfileSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        register_serializer = ClientRegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            client = register_serializer.save()

            # Autenticar al usuario recién creado
            login(request, client.user)
            client_dict = {'Name': client.user.username, 'Email': client.user.email}
            response = Response(
                {'success': 'User registered successfully',
                 'client': client_dict},
                status=status.HTTP_201_CREATED
            )
        else:
            response = Response({'error': register_serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        return response


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            # Obtener el nombre de usuario del usuario autenticado
            username = user.username
            return Response({'message': 'Inicio de sesión exitoso',
                             'token': token.key,'username': username}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(APIView):
    def get(self, request):
        try:
            client = Client.objects.get(user=request.user)
            serializer = ProfileSerializer(client) # toma el objeto Client y lo transforma en una representación serializada de los datos
            return Response(serializer.data)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)