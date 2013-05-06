from django.db import models
from django.contrib.auth.models import User
from nodes.models import Node

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user_id=models.ForeignKey(User)
    node_id=models.ForeignKey(Node)
    def __unicode__(self):
        return self.comment

    
    class Meta:
        db_table='Comment'
        app_label='participation'