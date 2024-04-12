from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country, Continent
from .serializers import CountrySerializer, ContinentSerializer


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

    @staticmethod
    def delete(request, num_code=None):
        if not num_code:
            return Response({'error': 'num_code is required'}, status=status.HTTP_400_BAD_REQUEST)
        country = Country.objects.filter(num_code=num_code).first()
        if not country:
            return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


