from rest_framework import serializers

from forum.models import VoyageThread, Comment
from main.models import Client


class ThreadSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)

    def create(self, validated_data):
        # Obtener el voyage_id de los datos validados
        voyage_id = self.context['voyage_id']
        # Obtener el usuario que ha creado el hilo
        user = self.context['request'].user
        # Obtener el foro del viaje
        client = Client.objects.filter(user=user).first()
        # Crear y guardar el hilo
        thread = VoyageThread.objects.create(
            title=validated_data['title'],
            created_by=client,
            voyage_id=voyage_id
        )
        return thread


class CommentSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=2056)

    def create(self, validated_data):
        # Obtener el voyage_id de los datos validados
        thread_id = self.context['thread_id']
        # Obtener el usuario que ha creado el hilo
        user = self.context['request'].user
        # Obtener el foro del viaje
        client = Client.objects.filter(user=user).first()
        # Crear y guardar el hilo
        thread = Comment.objects.create(
            content=validated_data['content'],
            client=client,
            thread_id=thread_id
        )
        return thread

