from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Layer(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_published =   models.BooleanField(default=True)
    is_external =   models.BooleanField(default=True)
    organization = models.CharField(blank=True,max_length=50)
    website = models.CharField(blank=True, max_length=50)
    center = models.PointField(null=True)
    area = models.PolygonField(null=True)
    write_access_level = models.IntegerField(blank=True, null=True)
    minimum_distance = models.IntegerField(blank=True, null=True)
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table='Layer'
        app_label='layers'
        
    