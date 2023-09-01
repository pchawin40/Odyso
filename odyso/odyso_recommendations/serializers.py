# odyso_recommendations/serializers.py
from rest_framework import serializers
from .models import Recommendations

class RecommendationsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recommendations
    fields = '__all__'
    
