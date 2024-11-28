from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models  
from django.contrib.auth.models import User  

class Task(models.Model):  
    title = models.CharField(max_length=255)  
    description = models.TextField(blank=True)  
    due_date = models.DateTimeField(null=True, blank=True)  
    is_overdue = models.BooleanField(default=False)  
    priority = models.CharField(max_length=50, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])  
    category = models.CharField(max_length=100)  
    state = models.CharField(max_length=50, choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('done', 'Done')])  
    owners = models.ManyToManyField(User, related_name='tasks')  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return self.title  

class Comment(models.Model):  
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)  
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return f"{self.user.username}: {self.content[:20]}"  

class Follow(models.Model):  
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)  
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)  

    def __str__(self):  
        return f"{self.follower.username} follows {self.following.username}"  