from rest_framework import serializers
from nodes.models import Node
from django.contrib.auth.models import User
from participation.models import Node_Rating_Count

class NodeSerializer(serializers.ModelSerializer):
    part = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Node
        fields = ('id', 'username', 'part')


class ParticipationSerializer(serializers.ModelSerializer):
    node= serializers.Field(source='node.name')
    
    class Meta:
        model=Node_Rating_Count
        fields= ('node','likes','dislikes','rating_avg','comment_count')
    
class ParticipationListSerializer(ParticipationSerializer):
    """ node participation """
    details = serializers.HyperlinkedIdentityField(view_name='node_participation_details')
    
    class Meta:
        model=Node_Rating_Count
        fields= ('node','details')
