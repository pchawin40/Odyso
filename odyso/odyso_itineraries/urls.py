# odyso_itineraries/urls.py
from django.urls import path
from .views import ItinerariesListCreateAPIView, UserItinerariesListAPIView, ItinerariesRetrieveUpdateDestroyAPIVIew

urlpatterns = [
  path('', ItinerariesListCreateAPIView.as_view(), name='itineraries-list-create'),
  # retrieve itineraries created by the current usr
  path('user', UserItinerariesListAPIView.as_view(), name='user-itineraries-list'),
  
  # retrieve itineraries by the given id
  path('<int:pk>', ItinerariesRetrieveUpdateDestroyAPIVIew.as_view(), name='itineraries-retrieve-update-destroy')
]
