from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,db_index=True)
    completed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
    
    def delete(self):
        self.deleted_at = datetime.now()
        self.save()

class TodoItem(models.Model):
    list = models.ForeignKey(TodoList,on_delete=models.CASCADE,related_name='todoitem')
    description = models.TextField()
    completed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.description
    def delete(self):
        self.deleted_at = datetime.now()
        self.save()