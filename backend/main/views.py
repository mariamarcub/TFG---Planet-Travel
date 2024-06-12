from django.contrib.auth import login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
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
                             'token': token.key, 'username': username}, status=status.HTTP_200_OK)
        else:
            # Manejar el caso de datos de inicio de sesión incorrectos
            error_message = "Nombre de usuario o contraseña incorrectos."
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)



class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        client = get_object_or_404(Client, user=request.user)
        serializer = ProfileSerializer(client) # toma el objeto Client y lo transforma en una representación serializada de los datos
        return Response(serializer.data)

    #Actualizar la información del perfil del usuario registrado
    def put(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            user = request.user
            user_data = serializer.validated_data['user']
            user.username = user_data.get('username', user.username)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.email = user_data.get('email', user.email)
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Para poder subir la imagen
    def post(self, request):
        client = get_object_or_404(Client, user=request.user)
        if 'photo' in request.FILES:
            client.photo = request.FILES['photo']
            client.save()
            return Response({'filePath': client.photo.url}, status=status.HTTP_200_OK)
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)


