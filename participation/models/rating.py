from django.db import models
from django.contrib.auth.models import User
from nodes.models import Node
#from choices import RATING_CHOICES

class Rating(models.Model):
    RATING_CHOICES= (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),

    

    
                    )
    rate = models.IntegerField(choices=RATING_CHOICES)
    user_id=models.ForeignKey(User)
    node_id=models.ForeignKey(Node)
  
    
    class Meta:
        db_table='Rating'
        app_label='participation'