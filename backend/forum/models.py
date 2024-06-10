from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from geo.models import Voyage
from main.models import Client


# Create your models here.


class VoyageThread(models.Model):
    title = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Client, on_delete=CASCADE)
    voyage = models.ForeignKey(Voyage, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "VoyagesThreads"


class Comment(models.Model):
    client = models.ForeignKey(Client, on_delete=CASCADE)
    content = models.CharField(max_length=2056)
    report_date = models.DateTimeField(default=timezone.now)
    thread = models.ForeignKey(VoyageThread, on_delete=CASCADE, null=True)

    def __str__(self):
        return f"{self.client.user.username} - {self.content} - {self.thread}"

    class Meta:
        verbose_name_plural = "Comments"
