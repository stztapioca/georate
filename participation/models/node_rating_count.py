from django.db import models
from nodes.models import Node

class NodeRatingCount(models.Model):
    node=models.OneToOneField(Node)
    likes =models.IntegerField (default=0)
    dislikes  =models.IntegerField (default=0)
    rating_count = models.IntegerField (default=0)
    rating_avg = models.FloatField (default=0.0)
    comment_count = models.IntegerField (default=0)
    def __unicode__(self):
        return self.node.name
    class Meta:
        db_table='NodeRatingCount'
        app_label='participation'
        
    