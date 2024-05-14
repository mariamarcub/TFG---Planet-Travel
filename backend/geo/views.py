# views.py
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main.models import Card, Client
from .models import Country, Continent, Voyage, Purchase
from .serializers import CountrySerializer, ContinentSerializer, MonthSerializer, AgeGroupSerializer, VoyageSerializer


#OBTENER LOS MESES DEL AÑO
class MonthAPIView(APIView):
    def get(self, request):
        # Obtener los meses disponibles en los viajes
        #meses = Voyage.objects.annotate(month=ExtractMonth('date')).values_list('month', flat=True).distinct()

        # Mapear los números de mes a sus nombres en español
        meses_dict = {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre'
        }
        # Obtener los números de mes disponibles
        meses = meses_dict.keys()
        # Convertir los números de mes a sus nombres correspondientes
        meses_disponibles = [{'id': mes, 'date': meses_dict[mes]} for mes in meses]

        serializer = MonthSerializer(data=meses_disponibles, many=True)
        serializer.is_valid()  # Validar los datos
        return Response(serializer.data)


#OBTENER TODOS LOS PAÍSES
class CountryAPIView(APIView):
    @staticmethod
    def get(request, num_code=None):
        if num_code:
            country = Country.objects.filter(num_code=num_code).first()
            if country:
                serializer = CountrySerializer(country)
                return Response(serializer.data)
            return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#OBTENER TODOS LOS CONTINENTES
class ContinentAPIView(APIView):
    @staticmethod
    def get(request, continent_id=None):
        if continent_id:
            continent = Continent.objects.filter(id=continent_id).first()
            if continent:
                serializer = ContinentSerializer(continent)
                return Response(serializer.data)
            return Response({'error': 'Continent not found'}, status=status.HTTP_404_NOT_FOUND)
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data)


#OBTENER LOS GRUPOS DE EDADES
class AgeGroupAPIView(APIView):
    def get(self, request):

        # Mapear los números de mes a sus nombres en español
        grupoEdad_dict = {
            1: '18 - 30',
            2: '30 - 45',
            3: '45+',
            4: 'Mixto',
            5: 'Todos',
        }
        # Obtener los números de mes disponibles
        grupoEdad = grupoEdad_dict.keys()
        # Convertir los números de mes a sus nombres correspondientes
        grupos_disponibles = [{'age': grupoEdad_dict[edad]} for edad in grupoEdad]

        serializer = AgeGroupSerializer(data=grupos_disponibles, many=True)
        serializer.is_valid()  # Validar los datos
        return Response(serializer.data)




#VISUALIZAR LOS VIAJES DEL MES SELECCIONADO
class MonthVoyageAPIView(APIView):
    def get(self, request, month):
        # Obtén el diccionario de meses desde la clase anterior
        voyages = Voyage.objects.filter(date_start__month=month).values(
            'id', 'country__name', 'date_start', 'date_end', 'description', 'itinerary', 'price', 'maximun_travelers'
        )
        voyages_list = list(voyages)
        if len(voyages) > 0:
            return Response(voyages_list, status=status.HTTP_200_OK)
        return Response({'Error': 'There are not voyages for this month.'},
                        status=status.HTTP_404_NOT_FOUND)


#VISUALIZA LA INFORMACIÓN DE UN VIAJE CONCRETO
class ShowVoyageInfoAPIView(APIView):
    def get(self, request, voyage_id):
        voyage = get_object_or_404(Voyage, pk=voyage_id)
        if voyage:
            data = {
                'voyage_info': voyage.itinerary,
                'voyage_date_start': voyage.date_start,
                'voyage_date_end': voyage.date_end,
                'description': voyage.description,
                'country_name': voyage.country.name,
                'voyage_price': voyage.price,
                'voyage_maximum_travelers': voyage.maximun_travelers
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'Error': 'Voyage not found'}, status=status.HTTP_404_NOT_FOUND)


#CREAR EL PROCESO DE COMPRA
class PurchaseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        voyage_id = request.POST['voyage']
        card_id = request.POST['card']
        voyage = get_object_or_404(Voyage, pk=voyage_id)
        card = get_object_or_404(Card, pk=card_id)
        user = request.user
        purchase = Purchase.objects.create(
            user=user,
            card=card,
            voyage=voyage
        )
        return Response({'message': f'Purchase created:{purchase.voyage.itinerary}'})


#CONFIRMAR LA COMPRA
class ConfirmPurchaseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, voyage_id):
        client = Client.objects.filter(user=request.user).first()
        voyage = get_object_or_404(Voyage, pk=voyage_id)
        cards = Card.objects.filter(client=client).values(
            'owner', 'expiration', 'cvv'
        )
        data = {
            'cards': list(cards),
            'client_name': client.user.username,
            'voyage_itinerary': voyage.itinerary,
            'voyage_date_start': voyage.date_start,
            'voyage_date_end': voyage.date_end,
            'voyage_price': voyage.price
        }
        return Response(data)