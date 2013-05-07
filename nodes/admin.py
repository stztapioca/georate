from django.contrib.gis import admin
#from django.contrib import admin
from models import Node,Node_Participation_Settings
from participation.models import Comment,Rating,Vote
from layers.models import Layer
class SettingsInLine(admin.TabularInline):
    model = Node_Participation_Settings
    extra = 1 
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1 
     
class RatingInLine(admin.TabularInline):
    model = Rating
    extra = 1 
class VoteInLine(admin.TabularInline):
    model = Vote
    extra = 1 
class NodeAdmin(admin.OSMGeoAdmin):
    fieldsets = [
        (None,               {'fields': ['name','slug','address','description']}),
        (Layer,               {'fields': ['layer_id','user_id']}),
        ('Map ', {'fields': ['coords'], 'classes': ['collapse']}),
    ]
    inlines = [SettingsInLine,CommentInLine,RatingInLine,VoteInLine]
    pnt = Point(12, 42, srid=4326)
    pnt.transform(900913)
    default_lon, default_lat = pnt.coords
#admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Node_Participation_Settings)
admin.site.register(Node, NodeAdmin)