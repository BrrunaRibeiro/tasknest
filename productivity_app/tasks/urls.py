from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import TaskViewSet, CommentViewSet, FollowViewSet  

router = DefaultRouter()  
router.register(r'tasks', TaskViewSet)  
router.register(r'comments', CommentViewSet)  
router.register(r'follow', FollowViewSet)  

urlpatterns = [  
    path('', include(router.urls)),  
] 