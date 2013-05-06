from django.db import models
from django.contrib.auth.models import User
from nodes.models import Node

class Vote(models.Model):
    VOTING_CHOICES=    (
        (1,'Like'),
        (-1,'Dislike'),
    )
    vote = models.IntegerField(choices=VOTING_CHOICES)
    user_id=models.ForeignKey(User)
    node_id=models.ForeignKey(Node)
  
    
    class Meta:
        db_table='Vote'
        app_label='participation'