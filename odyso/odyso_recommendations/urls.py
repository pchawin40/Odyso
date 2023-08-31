# odyso_recommendations/urls.py
from django.urls import path
from .views import RecommendationsListCreateAPIView, UserRecommendationsListAPIView

urlpatterns = [
  # retrieve all available itineraries
  path('', RecommendationsListCreateAPIView.as_view(), name='recommendations-list-create'),
  # retrieve itineraries created by the current usr
  path('user/', UserRecommendationsListAPIView.as_view(), name='user-recommendations-list')
]
