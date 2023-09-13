# Generated by Django 4.2.4 on 2023-09-02 03:38

from django.db import migrations, models
import django.db.models.deletion

# to link with itinerary as default for current recommendation
def set_default_itinerary(apps, schema_editor):
    Recommendations = apps.get_model('odyso_recommendations', 'Recommendations')
    Itineraries = apps.get_model('odyso_itineraries', 'Itineraries')
    
    default_itinerary = Itineraries.objects.first()
    
    for recommendation in Recommendations.objects.all():
        recommendation.itinerary = default_itinerary
        recommendation.save()

class Migration(migrations.Migration):

    dependencies = [
        ('odyso_itineraries', '0003_alter_itineraries_options'),
        ('odyso_recommendations', '0003_alter_recommendations_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendations',
            name='itinerary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='odyso_itineraries.itineraries'),
        ),
        migrations.RunPython(set_default_itinerary),
    ]
