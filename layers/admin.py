from django.contrib.gis import admin
from django.contrib.gis.geos import Point 
#from django.contrib import admin
from models import Layer,Layer_Participation_Settings

class SettingsInLine(admin.TabularInline):
    model = Layer_Participation_Settings
    extra = 1 

class LayerAdmin(admin.OSMGeoAdmin): 
    map_width = 300
    map_height = 200
    fieldsets = [
        (None,               {'fields': ['name','slug','description']}),
        ('Area', {'fields': ['area'], 'classes': ['collapse']}),
        ('Center', {'fields': ['center'], 'classes': ['collapse']}),
    ]
    inlines = [SettingsInLine]
    pnt = Point(12, 42, srid=4326)
    pnt.transform(900913)
    default_lon, default_lat = pnt.coords

#admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Layer, LayerAdmin)