from models import Node
from serializers import NodeSerializer
from rest_framework import generics
from rest_framework.views import APIView

class Node_List(generics.ListAPIView):
    model= Node
    serializer_class= NodeSerializer
