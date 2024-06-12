from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe

from main.models import Card, Client
from .models import Country, Continent, Voyage, Purchase, City, Opinion
from .serializers import CountrySerializer, ContinentSerializer, \
    MonthSerializer, AgeGroupSerializer, VoyageSerializer, \
    VoyagerSerializer


stripe.api_key = 'sk_test_51PIvXSGtzfLtviFbRhm1TMvJ4XiMdV2URKIwZsKtGFvy6oHVGGc3I0wpTQRcVDthyDV64iDlGhq0kneZ6o07lClD00yU38cBcW'


#OBTENER LOS MESES DEL AÑO
class MonthAPIView(APIView):
    def get(self, request):
        # Obtener los meses disponibles en los viajes
        #meses = Voyage.objects.annotate(month=ExtractMonth('date')).values_list('month', flat=True).distinct()
        print('a')
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


#VISUALIZAR LOS VIAJES DEL MES SELECCIONADO
class MonthVoyageAPIView(APIView):
    def get(self, request, month):
        # Obtén el diccionario de meses desde la clase anterior
        voyages = Voyage.objects.filter(date_start__month=month).values(
            'id', 'city__name', 'date_start', 'date_end', 'description',
            'itinerary', 'price', 'maximum_travelers', 'active_travelers', 'age_group'
        )
        voyages_list = list(voyages)
        if len(voyages) > 0:
            return Response(voyages_list, status=status.HTTP_200_OK)
        return Response({'Error': 'There are not voyages for this month.'},
                        status=status.HTTP_404_NOT_FOUND)


#VISUALIZA LOS VIAJES DE DICHO CONTINENTE
class ContinentVoyagesAPIView(APIView):
    def get(self, request, continent_id):
        continent = get_object_or_404(Continent, id=continent_id)
        voyages_in_continent = Voyage.objects.filter(
            city__country__continent=continent
        ).values(
            'id', 'city__name', 'date_start', 'date_end', 'description',
            'itinerary', 'price', 'maximum_travelers', 'active_travelers', 'age_group'
        )
        voyages_list = list(voyages_in_continent)
        if len(voyages_list) > 0:
            return Response(voyages_list, status=status.HTTP_200_OK)
        return Response({'Error': 'There are not voyages for this continent.'},
                        status=status.HTTP_404_NOT_FOUND)


#VIASUALIZAR LOS VIAJES POR EL GRUPO DE EDAD SELECCIONADO
class AgeGroupVoyagesAPIView(APIView):
    def get(self, request, age_group):
        # Obtén el diccionario de meses desde la clase anterior
        voyages = Voyage.objects.filter(age_group=age_group).values(
            'id', 'city__name', 'date_start', 'date_end', 'description',
            'itinerary', 'price', 'maximum_travelers', 'active_travelers', 'age_group'
        )
        voyages_list = list(voyages)
        if len(voyages) > 0:
            return Response(voyages_list, status=status.HTTP_200_OK)
        return Response({'Error': 'There are not voyages for this age group.'},
                        status=status.HTTP_404_NOT_FOUND)




#VISUALIZA LA INFORMACIÓN DE UN VIAJE CONCRETO
class ShowVoyageInfoAPIView(APIView):
    def get(self, request, voyage_id):
        voyage = get_object_or_404(Voyage, pk=voyage_id)
        client = get_object_or_404(Client, user=request.user)
        purchase = Purchase.objects.filter(
            client=client, voyage=voyage
        ).first()
        if voyage:
            data = {
                'voyage_id': voyage.id,
                'voyage_info': voyage.itinerary,
                'voyage_date_start': voyage.date_start,
                'voyage_date_end': voyage.date_end,
                'description': voyage.description,
                'city_name': voyage.city.name,
                'city_latitude': voyage.city.latitude,
                'city_longitude': voyage.city.longitude,
                'voyage_price': voyage.price,
                'voyage_maximum_travelers': voyage.maximum_travelers,
                'active_travelers': voyage.active_travelers,
                'age_group': voyage.age_group,
                'is_purchased': purchase is not None
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'Error': 'Voyage not found'}, status=status.HTTP_404_NOT_FOUND)




class PurchaseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        # Validar los datos del viajero
        voyager_data = request.data
        serializer = VoyagerSerializer(data=voyager_data)
        if serializer.is_valid():
            # Obtener y validar datos del viaje y número de viajeros
            try:
                voyage_id = request.data.get('voyageId')
                num_travelers = int(request.data.get('num_persons'))
            except (ValueError, TypeError) as e:
                return Response({'message': 'Datos inválidos para el número de personas o ID del viaje'}, status=400)

            # Obtener el viaje
            voyage = get_object_or_404(Voyage, pk=voyage_id)

            # Verificar que no se exceda el número máximo de viajeros
            if voyage.maximum_travelers < num_travelers + voyage.active_travelers:
                return Response({'message': 'Se ha excedido el número máximo de viajeros'}, status=400)

            # Obtener la tarjeta y el cliente
            card = Card.objects.filter(client__user=request.user).first()
            client = Client.objects.filter(user=request.user).first()

            # Calcular el monto total de la compra
            total_amount = voyage.price * num_travelers

            # Crear la compra
            purchase = Purchase.objects.create(
                client=client,
                card=card,
                voyage=voyage,
                amount=total_amount,  # Usar el monto total calculado
            )
            stripe.Charge.create(
                amount=int(total_amount * 100),
                currency='eur',
                description=f'Pago de {request.user.username} date {timezone.now()}',
                source=request.data.get('stripeToken')
            )
            # Actualizar el número de viajeros activos
            voyage.active_travelers += num_travelers
            voyage.save()

            return Response({'message': f'Compra creada: {purchase.voyage.itinerary}',
                             'total_amount': total_amount}, status=201)

            # Si el serializer no es válido, retornar los errores
        return Response(serializer.errors, status = 400)




#CONFIRMAR LA COMPRA
class ConfirmPurchaseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, voyage_id): #voyage_id se obtiene desde la URL
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


#RECOGE LOS VIAJES COMPRADOS POR CLIENTE

class VoyagesByClientAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        client = Client.objects.filter(user=request.user).first()
        voyages = Purchase.objects.filter(client=client).values(
            'voyage__id', 'voyage__city__name', 'voyage__date_start'
        ).distinct()
        return Response(voyages)




#OPINIONES DE LOS CLIENTES QUE HAN REALIZADO UN VIAJE
class OpinionsAPIView(APIView):
    def get(self, request):
        opinions = Opinion.objects.all().order_by(
            '-report_date')[:5]
        opinions_data = [{"rating": opinion.rating, "comment": opinion.comment,
                          "report_date": opinion.report_date} for opinion in
                         opinions]
        return Response(opinions_data)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        client = get_object_or_404(Client, user=request.user)
        voyage = get_object_or_404(Voyage, pk=request.data['voyage_id']) #Para coger la ID desde el navegador
        today = timezone.now().date()
        purchase = Purchase.objects.filter(
            client=client, voyage=voyage
        ).first()

        if purchase and today >= voyage.date_end:
            Opinion.objects.create(
                purchase=purchase,
                rating=int(request.data['opinion']['rating']),
                comment=request.data['opinion']['comment']
            )
            return Response({'message': 'Opinion created.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Error bad request.'}, status=status.HTTP_400_BAD_REQUEST)




