from models import Node
from serializers import NodeSerializer, NodeListSerializer
from rest_framework import generics
from rest_framework.views import APIView

class NodeList(generics.ListAPIView):
    """
    ### GET
    
    Retrieve a **list** of nodes
    """
    model= Node
    serializer_class= NodeListSerializer
    
class NodeDetail(generics.RetrieveAPIView):
    model= Node
    serializer_class= NodeSerializer
    
