from models import Layer
from serializers import LayerSerializer,LayerListSerializer,LayerNodeListSerializer
from rest_framework import generics
from rest_framework.views import APIView

class LayerList(generics.ListCreateAPIView):
    model= Layer
    serializer_class= LayerListSerializer
        
class LayerDetail(generics.RetrieveAPIView):
    model= Layer
    serializer_class= LayerSerializer
    
class LayerNodesDetail(generics.RetrieveAPIView):
    model= Layer
    serializer_class= LayerNodeListSerializer

