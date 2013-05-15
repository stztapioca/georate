from models import Node
from serializers import NodeSerializer, NodeListSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework import authentication


class NodeList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve a **list** of nodes
    """
    model= Node
    serializer_class= NodeListSerializer
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class NodeDetail(generics.RetrieveUpdateAPIView):
    model= Node
    serializer_class= NodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


from vectorformats.Formats import Django, GeoJSON
from rest_framework.response import Response
import simplejson as json

class NodeGeojsonList(generics.RetrieveAPIView):
    model= Node
    #serializer_class= NodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        n = Node.objects.all()
        djf = Django.Django(geodjango="coords", properties=['name', 'description'])
        geoj = GeoJSON.GeoJSON()
        s = geoj.encode(djf.decode(n))  
        return Response(json.loads(s))

NodeGeojson = NodeGeojsonList.as_view()

#def NodeGeojson(request):
#    from vectorformats.Formats import Django, GeoJSON
#    n = Node.objects.all()
#    djf = Django.Django(geodjango="coords", properties=['name', 'description'])
#    geoj = GeoJSON.GeoJSON()
#    s = geoj.encode(djf.decode(n))
#    return HttpResponse(s) 
