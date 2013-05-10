from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
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
     url(r'^api_v1/nodes/$', nodes.views.NodeList.as_view()),
     url(r'^api_v1/nodes/(?P<pk>[0-9]+)/$', nodes.views.NodeDetail.as_view(), name='api_node_details'),
     url(r'^api_v1/layers/$', layers.views.LayerList.as_view()),
     url(r'^api_v1/layers/(?P<pk>[0-9]+)/$', layers.views.LayerDetail.as_view()),
     url(r'^api_v1/comments', participation.views.Comment_List.as_view()),
     )
urlpatterns = format_suffix_patterns(urlpatterns)