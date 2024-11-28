from rest_framework import viewsets
from .models import Task, Comment, Follow
from .serializers import TaskSerializer, CommentSerializer, FollowSerializer

class TaskViewSet(viewsets.ModelViewSet):  
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer  

class CommentViewSet(viewsets.ModelViewSet):  
    queryset = Comment.objects.all()  
    serializer_class = CommentSerializer  

class FollowViewSet(viewsets.ModelViewSet):  
    queryset = Follow.objects.all()  
    serializer_class = FollowSerializer  