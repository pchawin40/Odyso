from django.contrib import admin
from .models import odyso_recommendations, odyso_safety_security, odyso_itineraries

# register models
admin.site.register(odyso_recommendations)
admin.site.register(odyso_safety_security)
admin.site.register(odyso_itineraries)
