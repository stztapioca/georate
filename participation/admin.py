from django.contrib import admin
from models import Vote,Rating,Comment

admin.site.register( Rating)
admin.site.register(Comment)
admin.site.register( Vote)