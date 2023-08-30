# odyso_recommendations/urls.py
from django.urls import path
from .views import RecommendationsListCreateAPIView

urlpatterns = [
  path('', RecommendationsListCreateAPIView.as_view(), name='recommendations-list-create')
]
