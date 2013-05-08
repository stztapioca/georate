from rest_framework import serializers
from models import Layer



        
class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Layer
        fields= ('name','slug','description','center','area' ,)
    
