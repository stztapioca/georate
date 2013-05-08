from models import Comment
from serializers import CommentSerializer
from rest_framework import generics
from rest_framework.views import APIView

class Comment_List(generics.ListAPIView):
    model= Comment
    serializer_class= CommentSerializer
