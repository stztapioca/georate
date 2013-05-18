from django.db import models
from django.contrib.auth.models import User
from nodes.models import Node
from participation.utils import is_participated
from django.db.models import Count, Min, Sum, Max, Avg
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
    user=models.ForeignKey(User)
    node=models.ForeignKey(Node)
    def save(self,*args,**kwargs):
        super(Rating,self).save()
        #node_id=self.node
        #a=self.node.id
        is_participated(self.node.id)
        n=self.node
        rating_count=n.rating_set.count()
        rating_avg=n.rating_set.aggregate(rate=Avg('rate'))
        rating_float=rating_avg['rate']
        nrc=n.noderatingcount
        nrc.rating_avg=rating_float
        nrc.rating_count=rating_count
        nrc.save()
    class Meta:
        db_table='Rating'
        app_label='participation'