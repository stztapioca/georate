from models import Comment
from nodes.models import Node
from rest_framework import generics
from rest_framework.views import APIView
from participation.models import NodeRatingCount
from serializers import ParticipationSerializer, ParticipationListSerializer,CommentSerializer,CommentNodeSerializer

class NodeParticipationList(generics.ListAPIView):
    """
    ### GET
    
    Retrieve a **list** of nodes
    """
    model= NodeRatingCount
    serializer_class= ParticipationListSerializer
    
class NodeParticipationDetail(generics.RetrieveAPIView):
    model= NodeRatingCount
    serializer_class= ParticipationSerializer

class CommentList(generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve a **list** of comments
    """
    model= Node
    serializer_class= CommentNodeSerializer   
    
#class CommentList(generics.RetrieveAPIView):
#    model= Comment
#    serializer_class= CommentListSerializer