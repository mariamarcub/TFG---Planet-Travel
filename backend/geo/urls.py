from django.conf import settings
from django.conf.urls.static import static


app_name = 'geo'

geo_urls = [
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)