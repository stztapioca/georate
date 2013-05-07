from django.contrib.gis import admin
#from django.contrib import admin
from models import Layer


class LayerAdmin(admin.GeoModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','slug','description']}),
        ('Area', {'fields': ['area'], 'classes': ['collapse']}),
        ('Center', {'fields': ['center'], 'classes': ['collapse']}),
    ]
    

#admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Layer, LayerAdmin)