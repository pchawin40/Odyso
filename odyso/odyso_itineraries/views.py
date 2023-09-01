# odyso_itineraries/views.py
from rest_framework import generics
from .models import Itineraries
from .serializers import ItinerariesSerializer
from rest_framework.permissions import IsAuthenticated

class ItinerariesListCreateAPIView(generics.ListCreateAPIView):
  queryset = Itineraries.objects.all()
  serializer_class = ItinerariesSerializer

# for obtaining queries from certain user
class UserItinerariesListAPIView(generics.ListAPIView):
  serializer_class = ItinerariesSerializer
  permission_classes = [IsAuthenticated]
  
  # retrieving query
  def get_queryset(self):
    return Itineraries.objects.filter(user=self.request.user)
