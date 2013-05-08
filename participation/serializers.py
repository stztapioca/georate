from rest_framework import serializers
from models import Comment
from nodes.models import Node
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'comments')

        
class CommentSerializer(serializers.ModelSerializer):
    user_id= serializers.Field(source='user_id.username')
    class Meta:
        model=Comment
        fields= ('comment','user_id')

    
