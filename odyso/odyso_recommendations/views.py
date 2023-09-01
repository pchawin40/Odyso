# odyso_recommendations/views.py
from rest_framework import generics
from .models import Recommendations
from .serializers import RecommendationsSerializer

# for obtaining all queries
class RecommendationsListCreateAPIView(generics.ListCreateAPIView):
  queryset = Recommendations.objects.all()
  serializer_class = RecommendationsSerializer
