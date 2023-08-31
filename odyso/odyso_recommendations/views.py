# odyso_recommendations/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Recommendations
from .serializers import RecommendationsSerializer

# for obtaining all queries
class RecommendationsListCreateAPIView(generics.ListCreateAPIView):
  queryset = Recommendations.objects.all()
  serializer_class = RecommendationsSerializer

# for obtaining queries from certain user
class UserRecommendationsListAPIView(generics.ListAPIView):
  serializer_class = RecommendationsSerializer
  permission_classes = [IsAuthenticated]
  
  # retrieving query
  def get_queryset(self):
    return Recommendations.objects.filter(user=self.request.user)
