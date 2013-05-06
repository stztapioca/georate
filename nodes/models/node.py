from django.contrib.gis.db import models
from django.contrib.auth.models import User
from layers.models import Layer


class Node(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50 ,unique=True)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    user_id=models.ForeignKey(User)
    layer_id=models.ForeignKey(Layer)
    is_published =   models.BooleanField(default=True)
    area = models.PolygonField()
    elevation = models.FloatField()
    external_id = models.IntegerField()
    notes = models.CharField(max_length=100)
    center = models.PointField()
    coords = models.PointField()
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table='Node'
        app_label='nodes'
        
    