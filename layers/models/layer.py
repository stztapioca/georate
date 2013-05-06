from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Layer(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_published =   models.BooleanField(default=True)
    is_external =   models.BooleanField(default=True)
    organization = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    center = models.PointField()
    area = models.PointField()
    write_access_level = models.IntegerField()
    minimum_distance = models.IntegerField()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table='Layer'
        app_label='layers'
        
    