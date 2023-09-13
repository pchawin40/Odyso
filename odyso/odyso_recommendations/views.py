# odyso_recommendations/views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import Recommendations
from odyso_itineraries.models import Itineraries
from .serializers import RecommendationsSerializer


# for obtaining all queries
class RecommendationsListCreateAPIView(generics.ListCreateAPIView):
  queryset = Recommendations.objects.all()
  serializer_class = RecommendationsSerializer

class UpvoteItineraryAPIView(generics.GenericAPIView):
  queryset = Itineraries.objects.all()
  lookup_url_kwarg = 'itinerary_id'
  lookup_field = 'id'
  serializer_class = RecommendationsSerializer
  
  def post(self, request, *args, **kwargs):
    # Fetch the Itinerary object
    itinerary = self.get_object()
    
    # Get related Recommendations object using Itinerary ID 
    recommendation = Recommendations.objects.get(id=itinerary.id)
    
    # Increment the upvote count or perform the required logic to handle upvote
    recommendation.upvotes += 1
    recommendation.save()
    
    # Return a custom response
    return Response({"message": "Successfully upvoted!"}, status=status.HTTP_200_OK)
