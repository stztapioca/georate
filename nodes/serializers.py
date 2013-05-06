from rest_framework import serializers
from nodes.models import Node
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    nodes = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nodes')
        
class NodeSerializer(serializers.ModelSerializer):
    user_id= serializers.Field(source='user_id.username')
    class Meta:
        model=Node
        fields= ('name','slug','user_id','address','area' ,'elevation','center' ,'coords',)
    
