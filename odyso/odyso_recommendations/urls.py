# odyso_recommendations/urls.py
from django.urls import path
from .views import RecommendationsListCreateAPIView, UpvoteItineraryAPIView

urlpatterns = [
  # retrieve all available itineraries
  path('', RecommendationsListCreateAPIView.as_view(), name='recommendations-list-create'),
  # update upvote for recommended itinerary
  path('upvote/<int:itinerary_id>/', UpvoteItineraryAPIView.as_view(), name='upvote-itinerary')
]
