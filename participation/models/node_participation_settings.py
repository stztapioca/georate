from django.db import models
from nodes.models import Node

class Node_Participation_Settings(models.Model):
    node=models.OneToOneField(Node)
    votings_allowed=models.BooleanField(default=True)
    comments_allowed=models.BooleanField(default=True)
    ratings_allowed=models.BooleanField(default=True)

    class Meta:
        db_table='Node_Participation_Settings'
        app_label='participation'
        
    