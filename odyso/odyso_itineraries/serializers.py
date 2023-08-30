# odyso_itineraries/serializers.py
from rest_framework import serializers
from .models import Itineraries

class ItinerariesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recommendations
    fields = '__all__'
