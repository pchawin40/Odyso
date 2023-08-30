from django.db import models
from django.conf import settings

"""
Database Schema:

Table Recommendations {
    id INT
    user_id INT [ref: > Users.id]
    recommendation_type ENUM('destination', 'activity')
    recommendation_data JSON
    upvotes INT
}
"""
# creating recommendation model
class Recommendations(models.Model):
  RECOMMENDATION_TYPES = [
    ('destination', 'Destination'),
    ('activity', 'Activity'),
  ]
  
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  recommendation_type = models.CharField(max_length=11, choices=RECOMMENDATION_TYPES)
  recommendation_data = models.JSONField()
  upvotes = models.IntegerField(default=0)
