from django.conf.urls import patterns, include, url
from nodes import views

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
     url(r'^api_v1/nodes', views.Node_List.as_view()),
     )
