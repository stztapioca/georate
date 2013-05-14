from rest_framework import serializers
from layers.models import Layer
from nodes.models import Node
from django.contrib.auth.models import User

class LayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Layer
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class NodeSerializer(serializers.ModelSerializer):
    user= serializers.Field(source='user.username')
    layer = serializers.Field(source='layer.name')
    class Meta:
        model=Node
        fields= ('layer','name','slug','user','area' ,'elevation','center' ,'coords',)
    
class NodeListSerializer(NodeSerializer):
    """ node list """
    details = serializers.HyperlinkedIdentityField(view_name='api_node_details')
        

    
    class Meta:
        model=Node
        fields= ('name', 'details')
