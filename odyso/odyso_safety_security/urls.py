# odyso_safety_security > urls.py

from django.urls import path
from .views import SafetyRoutesListCreateAPIView

urlpatterns = [
  path('', SafetyRoutesListCreateAPIView.as_view(), name='safety-routes-list-create')
]
