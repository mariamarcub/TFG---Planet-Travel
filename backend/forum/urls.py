from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from forum.views import ForoAPIView, ThreadAPIView, delete_thread, \
    delete_comment

app_name = 'forum'

urlpatterns = [
    path('forumVoyage/<int:voyage_id>', ForoAPIView.as_view(), name='forum'),
    path('forumVoyage', ForoAPIView.as_view(), name='forum'),
    path('forumVoyage/thread/<int:thread_id>', ThreadAPIView.as_view(), name='forum'),
    path('forumVoyage/delete-comment/<int:comment_id>', delete_comment, name='forum'),
    path('forumVoyage/delete-thread/<int:thread_id>', delete_thread, name='forum'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
