from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import RegisterAPIView, LoginAPIView, ProfileAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/registrarse/', RegisterAPIView.as_view(), name='registro'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('', include('geo.urls')),
    path('', include('forum.urls')),
]