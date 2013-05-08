from django.conf.urls import patterns, include, url
import nodes.views
import layers.views
import participation.views
#from layers import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'georate.views.home', name='home'),
    # url(r'^georate/', include('georate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^api_v1/nodes', nodes.views.Node_List.as_view()),
     url(r'^api_v1/layers', layers.views.Layer_List.as_view()),
     url(r'^api_v1/comments', participation.views.Comment_List.as_view()),
     )
