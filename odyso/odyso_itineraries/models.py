from django.db import models
from django.conf import settings

"""
  Table Itineraries {
    id INT
    user_id INT [ref: > Users.id]
    title VARCHAR
    description TEXT
    start_date DATE
    end_date DATE
    budget DECIMAL
}
"""

# creating itineraries model
class Itineraries(models.Model):
  # set up meta...
  class Meta:
    # to specifical plural form to use in admin interface
    verbose_name_plural = "Itineraries"
  
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length = 255) # VARCHAR is CharField 
  description = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
  budget = models.DecimalField(max_digits=10, decimal_places=2) 
