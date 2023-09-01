# odyso_recommendations/urls.py
from django.urls import path
from .views import RecommendationsListCreateAPIView

urlpatterns = [
  # retrieve all available itineraries
  path('', RecommendationsListCreateAPIView.as_view(), name='recommendations-list-create'),
]
