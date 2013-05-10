from django.db import models
from nodes.models import Node

class Node_Rating_Count(models.Model):
    node=models.OneToOneField(Node)
    likes =models.IntegerField (default=0)
    dislikes  =models.IntegerField (default=0)
    rating_avg = models.FloatField (default=0.0)
    comment_count = models.IntegerField (default=0)
    def __unicode__(self):
        return self.node.name
    class Meta:
        db_table='Node_Rating_Count'
        app_label='participation'
        
    