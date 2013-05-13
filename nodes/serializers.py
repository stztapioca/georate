from rest_framework import serializers
from nodes.models import Node
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    nodes = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nodes')


class NodeSerializer(serializers.ModelSerializer):
    user= serializers.Field(source='user.username')
    
    class Meta:
        model=Node
        fields= ('name','slug','user','area' ,'elevation','center' ,'coords',)
    
class NodeListSerializer(NodeSerializer):
    """ node list """
    details = serializers.HyperlinkedIdentityField(view_name='api_node_details')
    
    class Meta:
        model=Node
        fields= ('name','slug','user','area' ,'elevation','center' ,'coords', 'details')
