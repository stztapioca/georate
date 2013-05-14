from django.db import models
from django.contrib.auth.models import User
from nodes.models import Node
from participation.utils import is_participated


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user=models.ForeignKey(User)
    node=models.ForeignKey(Node)
    def __unicode__(self):
        return self.comment
    def save(self):
        super(Comment,self).save()
        #node_id=self.node
        #a=self.node.id
        is_participated(self.node.id)
        n=self.node
        comments=n.comment_set.count()
        nrc=n.noderatingcount
        nrc.comment_count=comments
        nrc.save()
        
    class Meta:
        db_table='Comment'
        app_label='participation'
        
        
    