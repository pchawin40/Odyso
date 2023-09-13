# odyso_itineraries/views.py
from rest_framework import generics
from .models import Itineraries
from .serializers import ItinerariesSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

# for obtaining query of a specific itinerary by its id
class ItinerariesRetrieveUpdateDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
  queryset = Itineraries.objects.all()
  serializer_class = ItinerariesSerializer
  
  lookup_field = 'pk'

  # for sending back message after delete request
  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    self.perform_destroy(instance)
    
    # customized message response
    return Response({"message": "Successfully deleted!"}, status=status.HTTP_200_OK)
