from django.db import models
from django.conf import settings
from odyso_itineraries.models import Itineraries

"""
Database Schema:


Table Recommendations {
    id INT
    user_id INT [ref: > Users.id]
    itinerary_id INT [ref: > Itineraries.id]
    recommendation_type ENUM('destination', 'activity')
    recommendation_data JSON
    upvotes INT
}
"""
# creating recommendation model
class Recommendations(models.Model):
  # set up meta...
  class Meta:
    # to specifical plural form to use in admin interface
    verbose_name_plural = "Recommendations"
  
  RECOMMENDATION_TYPES = [
    ('destination', 'Destination'),
    ('activity', 'Activity'),
  ]
  
  # foreign key that indicate which itinerary a recommendation belongs to
  itinerary = models.ForeignKey(Itineraries, null=True, on_delete=models.CASCADE)
  
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  recommendation_type = models.CharField(max_length=11, choices=RECOMMENDATION_TYPES)
  recommendation_data = models.JSONField()
  upvotes = models.IntegerField(default=0)
