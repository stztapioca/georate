from models import Comment
from rest_framework import generics
from rest_framework.views import APIView
from participation.models import Node_Rating_Count
from serializers import ParticipationSerializer, ParticipationListSerializer

class NodeParticipationList(generics.ListAPIView):
    """
    ### GET
    
    Retrieve a **list** of nodes
    """
    model= Node_Rating_Count
    serializer_class= ParticipationListSerializer
    
class NodeParticipationDetail(generics.RetrieveAPIView):
    model= Node_Rating_Count
    serializer_class= ParticipationSerializer