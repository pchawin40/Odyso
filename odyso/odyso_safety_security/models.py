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
  # set up meta...
  class Meta:
    # to specifical plural form to use in admin interface
    verbose_name_plural = "Safety Routes"
  
  itinerary = models.ForeignKey('odyso_itineraries.Itineraries', on_delete=models.CASCADE) 
  route_data = models.JSONField()
  safety_score = models.IntegerField(default=0)
