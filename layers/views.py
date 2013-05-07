from models import Layer
from serializers import LayerSerializer
from rest_framework import generics
from rest_framework.views import APIView

class Layer_List(generics.ListAPIView):
    model= Layer
    serializer_class= LayerSerializer
