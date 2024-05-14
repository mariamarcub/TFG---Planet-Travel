from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from geo.views import CountryAPIView, ContinentAPIView, MonthAPIView, AgeGroupAPIView, MonthVoyageAPIView, \
    ShowVoyageInfoAPIView, ConfirmPurchaseAPIView, PurchaseAPIView

app_name = 'geo'

geo_urls = [
    path('months/', MonthAPIView.as_view(), name='months'),
    path('monthTrips/<int:month>', MonthVoyageAPIView.as_view(), name='monthTrip'),
    path('showVoyage/<int:voyage_id>', ShowVoyageInfoAPIView.as_view(), name='ageGroup'),
    path('countries/', CountryAPIView.as_view(), name='countries'),
    path('country/<int:num_code>/', CountryAPIView.as_view(), name='country_by_num_code'),
    path('continents/', ContinentAPIView.as_view(), name='continents'),
    path('continent/<int:continent_id>/', ContinentAPIView.as_view(), name='continent_by_num_code'),
    path('ageGroup/', AgeGroupAPIView.as_view(), name='ageGroup'),
    path('confirmPurchase/<int:voyage_id>', ConfirmPurchaseAPIView.as_view(), name='ageGroup'),
    path('purchase-done/', PurchaseAPIView.as_view(), name='ageGroup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)