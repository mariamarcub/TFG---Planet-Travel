from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Client
from main.serializers import ClientSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        # Extraer los datos del cuerpo de la solicitud
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')

        # Validar que se proporcionaron todos los campos necesarios
        if not username or not first_name or not last_name or not password:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # Crear un nuevo usuario
            user = User.objects.create_user(username=username,
                                            first_name=first_name,
                                            last_name=last_name,
                                            password=password)

            # Crear un nuevo cliente asociado al usuario
            client = Client.objects.create(user=user)

            # Autenticar al usuario recién creado
            login(request, user)

            # Serializar el nuevo cliente
            serializer = ClientSerializer(client, many=True)

            return Response({'success': 'User registered successfully', 'client': serializer.data},
                            status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
