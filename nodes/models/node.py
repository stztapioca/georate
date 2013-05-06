from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Node(models.Model):
    name = models.CharField(max_length=50)
    user_id=models.ForeignKey(User)
    area = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    coords = models.PointField()
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table='Node'
        app_label='nodes'
        
    