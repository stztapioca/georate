from models import Comment
from nodes.models import Node
from rest_framework import generics
from rest_framework.views import APIView
from participation.models import NodeRatingCount
from serializers import NodeParticipationSerializer,NodeCommentSerializer

class NodeParticipationDetail(generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve participation details for a node
    """
    model= Node
    serializer_class= NodeParticipationSerializer
    
    
class NodeParticipationList(generics.ListAPIView):
    """
    ### GET
    
    Retrieve participation details for all nodes
    """
    model= Node
    serializer_class= NodeParticipationSerializer
    
class NodeCommentDetail(generics.RetrieveAPIView):
    """
    ### GET
    
    Retrieve a **list** of comments for a node
    """
    model= Node
    serializer_class= NodeCommentSerializer
    

class NodeCommentList(generics.ListAPIView):
    """
    ### GET
    
    Retrieve a **list** of comments for all nodes
    """
    model= Node
    serializer_class= NodeCommentSerializer
    
#class CommentList(generics.RetrieveAPIView):
#    """
#    ### GET
#    
#    Retrieve a **list** of comments
#    """
#    model= Node
#    serializer_class= NodeParticipationSerializer 
    
#class CommentList(generics.RetrieveAPIView):
#    model= Comment
#    serializer_class= CommentListSerializer