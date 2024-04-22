# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country, Continent, Voyage
from .serializers import CountrySerializer, ContinentSerializer, MonthSerializer, AgeGroupSerializer


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
    #
    # @staticmethod
    # def delete(request, num_code=None):
    #     if not num_code:
    #         return Response({'error': 'num_code is required'}, status=status.HTTP_400_BAD_REQUEST)
    #     country = Country.objects.filter(num_code=num_code).first()
    #     if not country:
    #         return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)
    #     country.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

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
