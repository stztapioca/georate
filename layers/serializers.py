from rest_framework import serializers
from models import Layer
        
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
    
