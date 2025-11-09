from django.db import models
from accounts.models import CustomUser

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message_text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Message from {self.name}"
        
