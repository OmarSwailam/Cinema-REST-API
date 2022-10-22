from dataclasses import fields
from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReservationSerializer(serializers.Serializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class GuestSerializer(serializers.Serializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'mobile', 'reservations']