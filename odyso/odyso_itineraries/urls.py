# odyso_itineraries/urls.py
from django.urls import path
from .views import ItinerariesListCreateAPIView

urlpatterns = [
  path('', ItinerariesListCreateAPIView.as_view(), name='itineraries-list-create')
]
