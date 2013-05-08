from django.db import models
from node import Node

class Node_Rating_Count(models.Model):
    node_id=models.OneToOneField(Node)
    likes =models.IntegerField (default=0)
    dislikes  =models.IntegerField (default=0)
    rating_avg = models.FloatField (default=0.0)
    comment_count = models.IntegerField (default=0)

    class Meta:
        db_table='Node_Rating_Count'
        app_label='nodes'
        
    