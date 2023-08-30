# odyso_safety_security/serializers.py

from rest_framework import serializers
from .models import SafetyRoutes

class SafetyRoutesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recommendations
    fields = '__all__'
