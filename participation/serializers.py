from rest_framework import serializers
from nodes.models import Node
from django.contrib.auth.models import User
from participation.models import NodeRatingCount,Comment


class UserSerializer(serializers.ModelSerializer):
    
    nodes = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id', 'username')



class CommentSerializer(serializers.ModelSerializer):
    
    username =serializers.Field(source='user.username')
    class Meta:
        model = Comment
        fields = ('username', 'comment')
        
        

class CommentNodeSerializer(serializers.ModelSerializer):
    
    #comments = serializers.PrimaryKeyRelatedField(many=True ,read_only=True)
    comments = CommentSerializer(source='comment_set')
    class Meta:
        model = Node
        fields = ('name','description','comments')

       
class ParticipationSerializer(serializers.ModelSerializer):
    
    node= serializers.Field(source='node.name')
    class Meta:
        model=NodeRatingCount
        fields= ('node','likes','dislikes','rating_avg','comment_count')

    
class ParticipationListSerializer(ParticipationSerializer):
    """ Node participation details"""
    details = serializers.HyperlinkedIdentityField(view_name='node_participation_details')
    class Meta:
        model=NodeRatingCount
        fields= ('node','details')
        
#class CommentListSerializer(serializers.ModelSerializer):
#    """ comment_list """
#    node= serializers.Field(source='node.name')
#    user= serializers.Field(source='user.username')
#    class Meta:
#        model=Comment
#        fields= ('node','user','comment')
