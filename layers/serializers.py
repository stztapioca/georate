from rest_framework import serializers
from models import Layer
from nodes.models import Node

class NodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Node
        fields = ('id','name', 'description')
        

class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Layer
        fields= ('name','slug','description','center','area' ,)
        

class LayerListSerializer(LayerSerializer):
    """ Layer list """
    details = serializers.HyperlinkedIdentityField(view_name='api_layer_details')
    
    class Meta:
        model=Layer
        fields= ('name','slug','description','center','area' ,'details',)
    
class LayerNodeListSerializer(LayerSerializer):
    """ Layer nodes """
    
    nodes = NodeSerializer(source='node_set')
    class Meta:
        model = Layer
        fields = ('name','nodes')
        