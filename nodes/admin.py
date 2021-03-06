from django.contrib.gis import admin
from django.contrib.gis.geos import Point

#from django.contrib import admin
from models import Node
from participation.models import Comment,Rating,Vote,NodeParticipationSettings,NodeRatingCount
from layers.models import Layer
class SettingsInLine(admin.TabularInline):
    model = NodeParticipationSettings
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
        (None,               {'fields': ['name','slug','description']}),
        (Layer,               {'fields': ['layer','user']}),
        ('Map ', {'fields': ['coords'], 'classes': ['collapse']}),
    ]
    inlines = [SettingsInLine,CommentInLine,RatingInLine,VoteInLine]
    pnt = Point(12, 42, srid=4326)
    pnt.transform(900913)
    default_lon, default_lat = pnt.coords
#admin.site.register(WorldBorder, admin.GeoModelAdmin)
#admin.site.register(Node_Participation_Settings)
admin.site.register(Node, NodeAdmin)
admin.site.register(NodeRatingCount)