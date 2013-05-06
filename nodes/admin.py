from django.contrib.gis import admin
#from django.contrib import admin
from models import Node,Node_Participation_Settings
from participation.models import Comment,Rating,Vote

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1 
     
class RatingInLine(admin.TabularInline):
    model = Rating
    extra = 1 
class VoteInLine(admin.TabularInline):
    model = Vote
    extra = 1 
class NodeAdmin(admin.GeoModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Map ', {'fields': ['coords'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInLine,RatingInLine,VoteInLine]

#admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Node_Participation_Settings)
admin.site.register(Node, NodeAdmin)