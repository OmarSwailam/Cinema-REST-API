from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    hall = models.CharField(max_length=10)
    date = models.DateField()


class Guest(models.Model):
    name = models.CharField(max_length=32)
    mobile = models.CharField(max_length=15)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name="reservations")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reservations")
    
