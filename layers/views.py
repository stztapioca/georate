from models import Layer
from serializers import LayerSerializer
from rest_framework import generics
from rest_framework.views import APIView

class LayerList(generics.ListCreateAPIView):
    model= Layer
    serializer_class= LayerSerializer
        
class LayerDetail(generics.RetrieveAPIView):
    model= Layer
    serializer_class= LayerSerializer
