# odyso_safety_security/views.py
from rest_framework import generics
from .models import SafetyRoutes
from .serializers import SafetyRoutesSerializer

class SafetyRoutesListCreateAPIView(generics.ListCreateAPIView):
  queryset = SafetyRoutes.objects.all()
  serializer_class = SafetyRoutesSerializer
