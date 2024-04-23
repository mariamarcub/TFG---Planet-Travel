from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.serializers import ClientRegisterSerializer, LoginSerializer


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
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)