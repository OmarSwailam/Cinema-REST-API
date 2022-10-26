from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Movie(models.Model):
    movie = models.CharField(max_length=100)
    hall = models.CharField(max_length=10)
    date = models.DateField()


class Guest(models.Model):
    name = models.CharField(max_length=32)
    mobile = models.CharField(max_length=15)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name="reservations")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reservations")
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)