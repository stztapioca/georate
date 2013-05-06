from django.db import models
from layer import Layer

class Layer_Participation_Settings(models.Model):
    layer_id=models.OneToOneField(Layer)
    votings_allowed=models.BooleanField(default=True)
    comments_allowed=models.BooleanField(default=True)
    ratings_allowed=models.BooleanField(default=True)

    class Meta:
        db_table='Layer_Participation_Settings'
        app_label='layers'
        
    