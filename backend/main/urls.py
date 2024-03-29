from django.urls import path, include
from rest_framework import routers
from main import views

router = routers.DefaultRouter()

#router.register(r'posts', views.PostViewSet,basename='post')
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls