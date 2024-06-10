from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from forum.models import VoyageThread, Comment
from forum.serializers import ThreadSerializer, CommentSerializer
from geo.models import Voyage


class ForoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, voyage_id):
        voyage = get_object_or_404(Voyage, id=voyage_id)
        threads = VoyageThread.objects.filter(
            voyage=voyage
        ).values('id', 'title', 'created_date', 'created_by__user__username')
        return Response(threads)

    def post(self, request, voyage_id=None):
        serializer = ThreadSerializer(data=request.data, context={'request': request, 'voyage_id': voyage_id})
        if serializer.is_valid():
            # Si los datos son válidos, crea el hilo
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Si los datos no son válidos, devuelve un error de validación
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ThreadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, thread_id):
        thread = get_object_or_404(VoyageThread, id=thread_id)
        comments = Comment.objects.filter(thread_id=thread_id).values(
            'id', 'client__user__username', 'content', 'report_date'
        ).order_by(
            '-report_date'
        )
        data_info = {
            'thread_title': thread.title,
            'comments': comments
        }
        return Response(data_info)

    def post(self, request, thread_id=None):
        serializer = CommentSerializer(data=request.data, context={'request': request, 'thread_id': thread_id})
        if serializer.is_valid():
            # Si los datos son válidos, crea el hilo
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Si los datos no son válidos, devuelve un error de validación
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_thread(request, thread_id):
    thread = get_object_or_404(VoyageThread, id=thread_id)
    if request.user != thread.created_by.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    thread.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.client.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

