from django.conf import settings
from django.db import models
from django.utils import timezone

class Theme(models.Model):
    name = models.CharField(max_length=200)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(default=2000)
    link = models.CharField(max_length=500)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return self.title