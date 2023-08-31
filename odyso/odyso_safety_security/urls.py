# odyso_safety_security > urls.py

from django.url import path
from .views import SafetyRoutesListCreateAPIView

urlpatterns = [
  pattern('', SafetyRoutesListCreateAPIView.as_view(), name='safety-routes-list-create')
]
