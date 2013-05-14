from models import Node
from serializers import NodeSerializer, NodeListSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse

class NodeList(generics.ListCreateAPIView):
    """
    ### GET
    
    Retrieve a **list** of nodes
    """
    model= Node
    serializer_class= NodeListSerializer
    
class NodeDetail(generics.RetrieveAPIView):
    model= Node
    serializer_class= NodeSerializer
    
def NodeGeojson(request):
    from vectorformats.Formats import Django, GeoJSON
    n = Node.objects.all()
    djf = Django.Django(geodjango="coords", properties=['name', 'description'])
    geoj = GeoJSON.GeoJSON()
    s = geoj.encode(djf.decode(n))
    return HttpResponse(s) 
