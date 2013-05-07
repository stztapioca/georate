from django.contrib.gis import admin
#from django.contrib import admin
from models import Layer,Layer_Participation_Settings

class SettingsInLine(admin.TabularInline):
    model = Layer_Participation_Settings
    extra = 1 

class LayerAdmin(admin.GeoModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','slug','description']}),
        ('Area', {'fields': ['area'], 'classes': ['collapse']}),
        ('Center', {'fields': ['center'], 'classes': ['collapse']}),
    ]
    inlines = [SettingsInLine]
   

#admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Layer, LayerAdmin)