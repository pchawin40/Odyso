# odyso_itineraries/views.py
from rest_framework import generics
from .models import Itineraries
from .serializers import ItinerariesSerializer

class ItinerariesListCreateAPIView(generics.ListCreateAPIView):
  queryset = Itineraries.objects.all()
  serializer_class = ItinerariesSerializer
