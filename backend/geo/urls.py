from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from geo.views import *

app_name = 'geo'

urlpatterns = [
    #Meses
    path('months/', MonthAPIView.as_view(), name='months'),
    path('monthTrips/<int:month>', MonthVoyageAPIView.as_view(), name='monthTrip'),

    #Continente
    path('continents/', ContinentAPIView.as_view(), name='continents'),
    path('continentTrips/<int:continent_id>/', ContinentVoyagesAPIView.as_view(), name='continent_by_num_code'),

    path('ageGroupTrips/<str:age_group>', AgeGroupVoyagesAPIView.as_view(), name='ageGroupTrips'),

    #Mostrar Viajes
    path('showVoyage/<int:voyage_id>', ShowVoyageInfoAPIView.as_view(), name='showVoyage'),

    #Compra
    path('confirmPurchase/<int:voyage_id>', ConfirmPurchaseAPIView.as_view(), name='confirmPurchase'),

    #Realizar Compra
    path('purchase-done/', PurchaseAPIView.as_view(), name='purchaseDone'),

    #Viajes comprados por el cliente
    path('voyagesByClient/', VoyagesByClientAPIView.as_view(), name='voyagesByClient'),

    #Opiniones de los clientes
    path('opinions/', OpinionsAPIView.as_view(), name='profile'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)