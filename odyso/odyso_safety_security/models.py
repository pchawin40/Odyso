from django.db import models
from django.conf import settings

"""
Database Schema:

Table SafetyRoutes {
    id INT
    itinerary_id INT [ref: > Itineraries.id]
    route_data JSON
    safety_score INT
}
"""
# creating safety models 
class SafetyRoutes(models.Model):
  itinerary = models.ForeignKey('odyso_itineraries.Itineraries', on_delete=models.CASCADE) 
  route_data = models.JSONField()
  safety_score = models.IntegerField(default=0)
