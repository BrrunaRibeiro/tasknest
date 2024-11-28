from rest_framework import serializers  
from .models import Task, Comment, Follow  

class TaskSerializer(serializers.ModelSerializer):  
    comments = serializers.StringRelatedField(many=True)  

    class Meta:  
        model = Task  
        fields = '__all__'  

class CommentSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Comment  
        fields = '__all__'  

class FollowSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Follow  
        fields = '__all__'  