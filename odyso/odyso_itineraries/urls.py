# odyso_itineraries/urls.py
from django.urls import path
from .views import ItinerariesListCreateAPIView, UserItinerariesListAPIView

urlpatterns = [
  path('', ItinerariesListCreateAPIView.as_view(), name='itineraries-list-create'),
  # retrieve itineraries created by the current usr
  path('user/', UserItinerariesListAPIView.as_view(), name='user-itineraries-list')
]
