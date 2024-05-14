from django.db import models
from django.db.models import CASCADE
from django.utils import timezone

from geo.models import Voyage
from main.models import Client


# Create your models here.


class Comment(models.Model):
    client = models.ForeignKey(Client, on_delete=CASCADE)
    comment = models.CharField(max_length=2056)
    report_date = models.DateTimeField(default=timezone.now)


class Forum(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=CASCADE)