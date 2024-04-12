from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from geo.views import CountryAPIView, ContinentAPIView

app_name = 'geo'

geo_urls = [
    path('countries/', CountryAPIView.as_view(), name='countries'),
    path('country/<int:num_code>/', CountryAPIView.as_view(), name='country_by_num_code'),
    path('continents/', ContinentAPIView.as_view(), name='continents'),
    path('continent/<int:continent_id>/', ContinentAPIView.as_view(), name='continent_by_num_code'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
