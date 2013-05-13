from django.contrib.gis.db import models
from django.contrib.auth.models import User
from layers.models import Layer


class Node(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50 ,unique=True)
    description = models.CharField(max_length=50)
    user=models.ForeignKey(User, null=True)
    layer=models.ForeignKey(Layer,null=True)
    is_published =   models.BooleanField(default=True)
    area = models.PolygonField(null=True)
    elevation = models.FloatField(null=True)
    external_id = models.IntegerField(null=True)
    notes = models.CharField(max_length=100,null=True)
    center = models.PointField(null=True)
    coords = models.PointField(null=True)
    objects = models.GeoManager()
    tags= models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table='Node'
        app_label='nodes'
        
    