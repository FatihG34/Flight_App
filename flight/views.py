from django.shortcuts import render
from .serializers import FlightSerializer, ReservationSerializer
from .models import Flight, Reservation, Passenger
from rest_framework import viewsets
from .permissions import IsStafForReadOnly
# Create your views here.

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafForReadOnly,)

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    