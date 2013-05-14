from django.db import models
from layer import Layer

class LayerParticipationSettings(models.Model):
    layer_id=models.OneToOneField(Layer)
    votings_allowed=models.BooleanField(default=True)
    comments_allowed=models.BooleanField(default=True)
    ratings_allowed=models.BooleanField(default=True)

    class Meta:
        db_table='LayerParticipationSettings'
        app_label='layers'
        
    