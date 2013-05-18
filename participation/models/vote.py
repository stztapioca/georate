from django.db import models
from django.contrib.auth.models import User
from nodes.models import Node
from participation.utils import is_participated

class Vote(models.Model):
    VOTING_CHOICES=    (
        (1,'Like'),
        (-1,'Dislike'),
    )
    vote = models.IntegerField(choices=VOTING_CHOICES)
    user=models.ForeignKey(User)
    node=models.ForeignKey(Node)
    def __unicode__(self):
        return self.node.name
    def save(self,*args,**kwargs):
        super(Vote,self).save()
        #node_id=self.node
        #a=self.node.id
        is_participated(self.node.id)
        n=self.node
        likes=n.vote_set.filter(vote=1).count()
        dislikes=n.vote_set.filter(vote=-1).count()
        nrc=n.noderatingcount
        nrc.likes=likes
        nrc.dislikes=dislikes
        nrc.save()
    
    class Meta:
        db_table='Vote'
        app_label='participation'